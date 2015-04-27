#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Companion software for rePaper
http://repaper.org

Developed for rePaper 2.7''
http://www.adafruit.com/products/1346

The MIT License (MIT)

Copyright (c) 2015 aerialist

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
from __future__ import print_function
import sys, time, os
import random

import serial
from serial.tools import list_ports
from PIL import Image, ImageOps
from PIL.ImageQt import ImageQt

from PyQt4.QtGui import *
from PyQt4.QtCore import *
MAC = True
try:
	from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
	MAC = False

from ui_repaperCompanion import Ui_MainWindow

VERSION = "v0.1"
APPNAME = "rePaper Companion"

def PILimageToQImage(pilimage):
	"""converts a PIL image to QImage
	This function is taken from 
	http://stackoverflow.com/questions/3041728/bug-when-drawing-a-qimage-on-a-widget-with-pil-and-pyqt
	"""
	imageq = ImageQt(pilimage) #convert PIL image to a PIL.ImageQt object
	qimage = QImage(imageq) #cast PIL.ImageQt object to QImage object -that´s the trick!!!
	return qimage

# CReader and CWriter are taken from sppyqt project by Eka A. Kurniawan
# https://code.google.com/p/sppyqt/source/browse/sppyqt.py
class CReader(QThread):
	def start(self, ser, priority = QThread.InheritPriority):
		self.ser = ser
		QThread.start(self, priority)
		
	def run(self):
		while True:
			try:
				data = self.ser.read(1)
				n = self.ser.inWaiting()
				if n:
					data = data + self.ser.read(n)
				self.emit(SIGNAL("newData(QString)"), data)
			except:
				errMsg = "Reader thread is terminated unexpectedly."
				self.emit(SIGNAL("error(QString)"), errMsg)
				break

class CWriter(QThread):
	def start(self, ser, cmd = "", priority = QThread.InheritPriority):
		self.ser = ser
		self.cmd = cmd
		QThread.start(self, priority)
		
	def run(self):
		try:
			self.ser.write(str(self.cmd))
		except:
			errMsg = "Writer thread is terminated unexpectedly."
			self.emit(SIGNAL("error(QString)"), errMsg)

	def terminate(self):
		self.wait()
		QThread.terminate(self)

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.setWindowTitle("{} {}".format(APPNAME, VERSION))
		self.sectorChanged()
		
		# Define rePaper devices and select 2.7'' as default
		device27 = {'name': "rePaper 2.7''",
				'size': (264, 176)}
		device20 = {'name': "rePaper 2.0''",
				'size': (200, 96)}
		device144 = {'name': "rePaper 1.44''",
				'size': (128, 96)}
		self.devices = [device27, device20, device144]
		for device in self.devices:
			self.comboBoxDevice.addItem(str(device['name']))
		self.onDeviceActivated()

		#self.view = GraphicsView() # Promoted in QtDesigner
		self.scene = QGraphicsScene(self)
		self.scene.setBackgroundBrush(QBrush(Qt.white, Qt.SolidPattern))
		self.scene.setSceneRect(0,0,self.epdSize[0],self.epdSize[1])
		self.view.setScene(self.scene)
		self.frameRect = None
		self.addFrameRect()
		
		self.reader = CReader()
		self.writer = CWriter()
		self.serial = None
		self.im = None
		self.readyMsg = 'Command: '
		self.lastmsg = ''

		self.connectPushButton.clicked.connect(self.toggleConnection)
		self.sendPushButton.clicked.connect(self.sendImg)
		self.saveXBMpushButton.clicked.connect(self.saveXBM)
		self.pushButtonAdd.clicked.connect(self.selectFile)
		self.pushButtonPaste.clicked.connect(self.imPaste)
		self.pushButtonRotate.clicked.connect(self.imRotate)
		self.pushButtonPreview.clicked.connect(self.imPreview)
		self.sectorSpinBox.valueChanged.connect(self.sectorChanged)
		self.randomPushButton.clicked.connect(self.randamizeSector)
		self.ePushButton.clicked.connect(lambda: self.sendCommand('e'))
		self.qdPushButton.clicked.connect(lambda: self.sendCommand('qd'))
		self.dPushButton.clicked.connect(lambda: self.sendCommand('d'))
		self.iPushButton.clicked.connect(lambda: self.sendCommand('i'))
		self.zPushButton.clicked.connect(lambda: self.sendCommand('z'))
		self.wPushButton.clicked.connect(lambda: self.sendCommand('w'))
		self.lPushButton.clicked.connect(lambda: self.sendCommand('l'))
		self.fPushButton.clicked.connect(lambda: self.sendCommand('f'))
		self.tPushButton.clicked.connect(lambda: self.sendCommand('t'))
		self.uPushButton.clicked.connect(lambda: self.sendCommand('u'))
		self.cmdSendPushButton.clicked.connect(self.sendCmd)
		self.comboBoxDevice.activated.connect(self.onDeviceActivated)
		
		self.connect(self.reader, SIGNAL("newData(QString)"), self.updateSerMonitor)
		self.connect(self.reader, SIGNAL("error(QString)"), self.printMsg)
		self.connect(self.writer, SIGNAL("error(QString)"), self.printMsg)

		# z command requires modified flash.c and flash.h to erase whole flash memory		
		self.zPushButton.hide()
		
		self.popuratePorts()
		self.randamizeSector()

	def onDeviceActivated(self):
		device = self.devices[self.comboBoxDevice.currentIndex()]
		self.epdSize = device['size']
		
	def addFrameRect(self):
		""" Rectanble to indicate device size
		"""
		if self.frameRect:
			self.removeFrameRect()
		self.frameRect = self.scene.addRect(0,0,self.epdSize[0],self.epdSize[1])

	def removeFrameRect(self):
		if self.frameRect:
			self.scene.removeItem(self.frameRect)
			self.frameRect = None

	def imPaste(self):
		self.removeFrameRect()
		qim = QApplication.clipboard().image()
		self.createPixmapItem(QPixmap.fromImage(qim), self.position())
		self.addFrameRect()
		
	def imRotate(self):
		for item in self.scene.selectedItems():
			item.setRotation(item.rotation()-30)
	
	def imPreview(self):
		""" send image in target area for preview
		"""
		# clean the area
		selectedItems = self.scene.selectedItems()
		self.scene.clearSelection()
		self.removeFrameRect()
		# TODO: use temp file object?
		fname = u"tmp.png"
		qim = QImage(self.epdSize[0],self.epdSize[1],QImage.Format_RGB32)
		qpain = QPainter(qim)
		qpain.setRenderHint(QPainter.Antialiasing)
		self.scene.render(qpain)
		qpain.end()
		qim.save(fname)
		self.im = Image.open(fname)
		self.showPreview()
		# bring back frame and selection
		self.addFrameRect()
		for item in selectedItems:
			item.setSelected(True)

	def createPixmapItem(self, pixmap, position, matrix=QMatrix()):
		item = QGraphicsPixmapItem(pixmap)
		item.setFlags(QGraphicsItem.ItemIsSelectable|
					  QGraphicsItem.ItemIsMovable)
		item.setPos(position)
		item.setMatrix(matrix)
		self.scene.clearSelection()
		self.scene.addItem(item)
		item.setSelected(True)

	def sectorChanged(self):
		imCount = int(self.sectorSpinBox.value())*2
		self.sectorHex1 = "{:02X}".format(imCount)
		self.sectorHex2 = "{:02X}".format(imCount+1)
		self.sectorLabel.setText("Target Sector: {} {}".format(self.sectorHex1, self.sectorHex2))
		
	def randamizeSector(self):
		self.sectorSpinBox.setValue(random.randrange(self.sectorSpinBox.maximum()))
		
	def popuratePorts(self):
		self.ports = list_ports.comports()
		for port in self.ports:
			self.comboBox.addItem(str(port[0]))

	def toggleConnection(self):
		if self.serial:
			self.stopThreads()
			self.serial.close()
			self.connectPushButton.setText("Connect")
			self.serial = None
		else:
			try:
				addr = self.ports[self.comboBox.currentIndex()][0]
				self.serial = serial.Serial(addr) # N81
				self.startReader(self.serial)
				self.connectPushButton.setText("Disconnect")
			except:
				self.printMsg("Failed to connect!")
		self.popuratePorts()
				
	def serialWrite(self, cmd):
		self.statusBar().showMessage("Working hard...")
		self.ready = False
		self.writer.start(self.serial, cmd)

	def startReader(self, serial):
		self.reader.start(serial)
		
	def stopThreads(self):
		self.stopReader()
		self.stopWriter()
		
	def stopReader(self):
		if self.reader.isRunning():
			self.reader.terminate()
			
	def stopWriter(self):
		if self.writer.isRunning():
			self.writer.terminate()
			
	def selectFile(self):
		fname = QFileDialog.getOpenFileName(
			self, 'Open File', '', 'Images (*.png *.bmp *.jpg *.jpeg)')
		if fname:
			self.bestFitImg(fname)
			self.showPreview()
			self.removeFrameRect()
			# Anaconda's Qt fail to load jpeg plugin?
			qpixmap = QPixmap(fname)
			if qpixmap.size().width() == 0:
				# QPixmap failed to load the image. Fall back to Pillow
				im = Image.open(unicode(fname))
				qim = PILimageToQImage(im)
				qpixmap = QPixmap.fromImage(qim)
			self.createPixmapItem(qpixmap, self.position())
			self.addFrameRect()
	
	def bestFitImg(self, fname):
			try:
				im = Image.open(unicode(fname))
			except:
				self.printMsg("Error opening: {}".format(fname))
			else:
				print(im.size)
				im_w, im_h = im.size
				if im_w < im_h:
					im = im.rotate(90)
					im_w, im_h = im.size
				print(im_w, im_h)
				aspect = float(im_w) / float(im_h)
				print(aspect)
				panelAspect = float(self.epdSize[0]) / float(self.epdSize[1])
				if aspect > panelAspect:
					newsize = (self.epdSize[0], int(self.epdSize[0]/aspect))
				else:
					newsize = (int(self.epdSize[1]*aspect), self.epdSize[1])
				print(newsize)
				im = im.resize(newsize)
				im_w, im_h = im.size
				background = Image.new('RGB', self.epdSize, (255, 255, 255))
				bg_w, bg_h = background.size
				offset = ((bg_w - im_w) / 2, (bg_h - im_h) / 2)
				background.paste(im, offset)
				im = background
				im = ImageOps.grayscale(im)
				self.im = im # must apply invert and convert("1") for epaper
				
	def showPreview(self):
		#im = ImageOps.invert(self.im)
		im = self.im.convert("1", dither=Image.FLOYDSTEINBERG)	
		# QPixmap doesn't like mode="1". 
		im2show = im.convert("L")
		qim = PILimageToQImage(im2show)
		pm = QPixmap(qim)
		self.imageLabel.setPixmap(pm)

	def position(self):
		point = self.mapFromGlobal(QCursor.pos())
		if not self.view.geometry().contains(point):
			coord = random.randint(36, 144)
			point = QPoint(coord, coord)
		else:
			self.addOffset = 5
			self.prevPoint = point
		return self.view.mapToScene(point)

	def saveXBM(self):
		if self.im:
			outname = QFileDialog.getSaveFileName(
				self, 'Save File', '', 'XBM (*.xbm)')
			if not outname:
				return None
			im = ImageOps.invert(self.im)
			im = im.convert("1", dither=Image.FLOYDSTEINBERG)	
			#outname = os.path.splitext(unicode(self.lineEdit.text()))[0] + ".xbm"
			im.save(outname)
			self.printMsg("image saved as {}".format(outname))
			
	def sendCmd(self):
		cmd = unicode(self.cmdLineEdit.text())
		if cmd:
			self.serialWrite(cmd)
			
	def sendCommand(self, command):
		if self.serial:
			if command == 'e':
				for sector in [self.sectorHex1, self.sectorHex2]:
					msg = "{}{} ".format(command, sector)
					self.printMsg(msg + ": Erase sector")
					self.serialWrite(msg)
					time.sleep(1)
			elif command == 'u':
				if not self.im:
					self.printMsg("Select an image first!")
					return None
				im = ImageOps.invert(self.im)
				im = im.convert("1", dither=Image.FLOYDSTEINBERG)	
				# TODO: Can tmpfile be used? im.save requires f to be oped in 'wb' mode but I want to send serial in ascii. How to do?
				fname = "tmp.xbm"
				im.save(fname) 
				msg = "{}{} ".format(command, self.sectorHex1)
				self.printMsg(msg + ": Upload image to sector")
				self.serialWrite(msg)
				time.sleep(1)
				with open(fname) as f:
					self.serialWrite(f.read())
				time.sleep(1)
			elif command == 'd':
				for sector in [self.sectorHex1, self.sectorHex2]:
					msg = "{}{} ff ".format(command, sector)
					self.printMsg(msg + ": Dump sector")
					self.serialWrite(msg)
					time.sleep(1)
			elif command == 'qd':
				for sector in [self.sectorHex1, self.sectorHex2]:
					msg = "{}{} 0f ".format('d', sector)
					self.printMsg(msg + ": Dump sector first Byte")
					self.serialWrite(msg)
					time.sleep(1)
			elif command == 'i':
				msg = "{}{} ".format(command, self.sectorHex1)
				self.printMsg(msg + ": Display an image")
				self.serialWrite(msg)
			elif command == 'z':
				msg = "z"
				self.printMsg(msg + ": Erase entire FLASH chip")
				self.serialWrite(msg)
			elif command == 'w':
				msg = command
				self.printMsg(msg + ": Clear display")
				self.serialWrite(msg)
				time.sleep(1)
			elif command == 'l':
				msg = command
				self.printMsg(msg + ": Search for non-empty sectors")
				self.serialWrite(msg)
			elif command == 'f':
				msg = command
				self.printMsg(msg + ": Dump FLASH identification")
				self.serialWrite(msg)
			elif command == 't':
				msg = command
				self.printMsg(msg + ": Show temperature")
				self.serialWrite(msg)
			else:
				self.printMsg("Unknown command: {}".format(command))
		else:
			self.printMsg("Connect first!")

	def eraseSegment(self, segment):
		msg = "e{:02X} ".format(segment)
		self.printMsg(msg + ": Erase segment")
		self.serialWrite(msg)
		time.sleep(10)
		msg = "e{:02X} ".format(segment+1)
		self.serialWrite(msg)
		time.sleep(10)
		
	def sendImg(self):
		if self.im:
			self.sendCommand('f') # FLASH identifiation
			self.sendCommand('e') # erase segment
			time.sleep(1)
			self.sendCommand('e') # erase segment jsut to make sure
			#self.sendCommand('w') # clear display
			self.sendCommand('u') # upload image
			self.sendCommand('i') # display image
		else:
			printMsg("Choose image file first!")
		
	def closeEvent(self, event):
		if self.serial:
			self.serial.close()

	def printMsg(self, msg):
		print(msg)
		self.logPlainTextEdit.appendPlainText(msg)
		self.logPlainTextEdit.moveCursor(QTextCursor.End)
		
	def updateSerMonitor(self, msg):
		# TODO: UI doesn't messages as commands are sent...
		# use Thread or Que?
		self.plainTextEdit.moveCursor(QTextCursor.End)
		self.plainTextEdit.insertPlainText(msg)
		self.plainTextEdit.moveCursor(QTextCursor.End)
		
		#self.readyMsg = 'Command: '
		#self.readyCount = 0
		# TODO: make this ready message work.
		if self.readyMsg in self.lastmsg+msg:
			self.ready = True
			self.statusBar().showMessage("Ready!")
		else:
			self.lastmsg = msg

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = MainWindow()
	form.show()
	app.exec_()
