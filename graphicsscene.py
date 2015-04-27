# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 18:02:43 2015

@author: aerialsit
"""

from __future__ import print_function

import random
import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class GraphicsView(QGraphicsView):
	def __init__(self, parent=None):
		super(GraphicsView, self).__init__(parent)
		self.setDragMode(QGraphicsView.RubberBandDrag)
		self.setRenderHint(QPainter.Antialiasing)
		self.setRenderHint(QPainter.TextAntialiasing)
		
	def wheelEvent(self, event):
		factor = 1.41 ** (-event.delta() / 240.0)
		# scale child pixitem instead of self
		#self.scale(factor, factor)
		for item in self.scene().selectedItems():
			item.setScale(item.scale()*factor)
		
	def keyPressEvent(self, event):
		key = event.key()
		if event.modifiers() & Qt.ShiftModifier:
			delta = 1
		else:
			delta = 10
			
		if key == Qt.Key_Delete or key == Qt.Key_Backspace:
			for item in self.scene().selectedItems():
				self.scene().removeItem(item)
		elif key == Qt.Key_Left:
			for item in self.scene().selectedItems():
				item.moveBy(-delta,0)
		elif key == Qt.Key_Right:
			for item in self.scene().selectedItems():
				item.moveBy(delta,0)
		elif key == Qt.Key_Up:
			for item in self.scene().selectedItems():
				item.moveBy(0,-delta)
		elif key == Qt.Key_Down:
			for item in self.scene().selectedItems():
				item.moveBy(0,delta)
	
class MainForm(QDialog):
	def __init__(self, parent=None):
		super(MainForm, self).__init__(parent)
		self.view = GraphicsView()
		self.scene = QGraphicsScene(self)
		self.scene.setSceneRect(0,0,264,176)
		self.view.setScene(self.scene)
		self.saveBtn = QPushButton("Save")
		self.saveBtn.clicked.connect(self.saveImage)
		layout = QHBoxLayout()
		layout.addWidget(self.view, 1)
		layout.addWidget(self.saveBtn)
		self.setLayout(layout)
		self.filename = u""
		#self.filename = QString()
		self.prevPoint = QPoint()
		self.addPixmap()
		self.scene.addRect(0,0,264,176)
		
	def saveImage(self):
		qim = QImage(264,176,QImage.Format_RGB32)
		qpain = QPainter(qim)
		qpain.setRenderHint(QPainter.Antialiasing)
		self.scene.render(qpain)
		qpain.end()
		qim.save("saved.png")

	def addPixmap(self):
		path = (QFileInfo(self.filename).path()
				if not self.filename else ".")
		fname = QFileDialog.getOpenFileName(self,
				"Page Designer - Add Pixmap", path,
				"Pixmap Files (*.bmp *.jpg *.jpeg *.png *.xbm *.xpm)")
		if not fname:
			return
		self.createPixmapItem(QPixmap(fname), self.position())
		#self.createPixmapItem(QPixmap(fname), self.view.mapToScene(QPoint(0,0)))
		#self.scene.addPixmap(QPixmap(fname))

	def createPixmapItem(self, pixmap, position, matrix=QMatrix()):
		item = QGraphicsPixmapItem(pixmap)
		item.setFlags(QGraphicsItem.ItemIsSelectable|
					  QGraphicsItem.ItemIsMovable)
		item.setPos(position)
		item.setMatrix(matrix)
		self.scene.clearSelection()
		self.scene.addItem(item)
		item.setSelected(True)

	def position(self):
		point = self.mapFromGlobal(QCursor.pos())
		if not self.view.geometry().contains(point):
			coord = random.randint(36, 144)
			point = QPoint(coord, coord)
		else:
			self.addOffset = 5
			self.prevPoint = point
		return self.view.mapToScene(point)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = MainForm()
	rect = QApplication.desktop().availableGeometry()
	form.resize(int(rect.width() * 0.6), int(rect.height() * 0.9))
	form.show()
	app.exec_()


