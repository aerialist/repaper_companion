# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/shunya/Dropbox/workspace/Python/eHayashiya/repaperCompanion.ui'
#
# Created: Mon Apr 27 17:53:27 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(788, 602)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.connectPushButton = QtGui.QPushButton(self.centralwidget)
        self.connectPushButton.setObjectName(_fromUtf8("connectPushButton"))
        self.horizontalLayout_2.addWidget(self.connectPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboBoxDevice = QtGui.QComboBox(self.centralwidget)
        self.comboBoxDevice.setObjectName(_fromUtf8("comboBoxDevice"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBoxDevice)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.imageLabel = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMinimumSize(QtCore.QSize(264, 176))
        self.imageLabel.setObjectName(_fromUtf8("imageLabel"))
        self.verticalLayout_2.addWidget(self.imageLabel)
        self.sendPushButton = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sendPushButton.setFont(font)
        self.sendPushButton.setObjectName(_fromUtf8("sendPushButton"))
        self.verticalLayout_2.addWidget(self.sendPushButton)
        self.saveXBMpushButton = QtGui.QPushButton(self.centralwidget)
        self.saveXBMpushButton.setObjectName(_fromUtf8("saveXBMpushButton"))
        self.verticalLayout_2.addWidget(self.saveXBMpushButton)
        self.logPlainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.logPlainTextEdit.setObjectName(_fromUtf8("logPlainTextEdit"))
        self.verticalLayout_2.addWidget(self.logPlainTextEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButtonAdd = QtGui.QPushButton(self.tab)
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.horizontalLayout_3.addWidget(self.pushButtonAdd)
        self.pushButtonPaste = QtGui.QPushButton(self.tab)
        self.pushButtonPaste.setObjectName(_fromUtf8("pushButtonPaste"))
        self.horizontalLayout_3.addWidget(self.pushButtonPaste)
        self.pushButtonRotate = QtGui.QPushButton(self.tab)
        self.pushButtonRotate.setObjectName(_fromUtf8("pushButtonRotate"))
        self.horizontalLayout_3.addWidget(self.pushButtonRotate)
        self.pushButtonPreview = QtGui.QPushButton(self.tab)
        self.pushButtonPreview.setObjectName(_fromUtf8("pushButtonPreview"))
        self.horizontalLayout_3.addWidget(self.pushButtonPreview)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.view = GraphicsView(self.tab)
        self.view.setObjectName(_fromUtf8("view"))
        self.verticalLayout_4.addWidget(self.view)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.sectorLabel = QtGui.QLabel(self.groupBox)
        self.sectorLabel.setObjectName(_fromUtf8("sectorLabel"))
        self.gridLayout.addWidget(self.sectorLabel, 0, 0, 1, 1)
        self.sectorSpinBox = QtGui.QSpinBox(self.groupBox)
        self.sectorSpinBox.setMaximum(128)
        self.sectorSpinBox.setProperty("value", 37)
        self.sectorSpinBox.setObjectName(_fromUtf8("sectorSpinBox"))
        self.gridLayout.addWidget(self.sectorSpinBox, 0, 1, 1, 1)
        self.randomPushButton = QtGui.QPushButton(self.groupBox)
        self.randomPushButton.setObjectName(_fromUtf8("randomPushButton"))
        self.gridLayout.addWidget(self.randomPushButton, 0, 2, 1, 1)
        self.qdPushButton = QtGui.QPushButton(self.groupBox)
        self.qdPushButton.setObjectName(_fromUtf8("qdPushButton"))
        self.gridLayout.addWidget(self.qdPushButton, 1, 0, 1, 1)
        self.dPushButton = QtGui.QPushButton(self.groupBox)
        self.dPushButton.setObjectName(_fromUtf8("dPushButton"))
        self.gridLayout.addWidget(self.dPushButton, 1, 2, 1, 1)
        self.uPushButton = QtGui.QPushButton(self.groupBox)
        self.uPushButton.setObjectName(_fromUtf8("uPushButton"))
        self.gridLayout.addWidget(self.uPushButton, 2, 0, 1, 2)
        self.ePushButton = QtGui.QPushButton(self.groupBox)
        self.ePushButton.setObjectName(_fromUtf8("ePushButton"))
        self.gridLayout.addWidget(self.ePushButton, 2, 2, 1, 1)
        self.wPushButton = QtGui.QPushButton(self.groupBox)
        self.wPushButton.setObjectName(_fromUtf8("wPushButton"))
        self.gridLayout.addWidget(self.wPushButton, 3, 0, 1, 2)
        self.iPushButton = QtGui.QPushButton(self.groupBox)
        self.iPushButton.setObjectName(_fromUtf8("iPushButton"))
        self.gridLayout.addWidget(self.iPushButton, 3, 2, 1, 1)
        self.fPushButton = QtGui.QPushButton(self.groupBox)
        self.fPushButton.setObjectName(_fromUtf8("fPushButton"))
        self.gridLayout.addWidget(self.fPushButton, 4, 0, 1, 1)
        self.tPushButton = QtGui.QPushButton(self.groupBox)
        self.tPushButton.setObjectName(_fromUtf8("tPushButton"))
        self.gridLayout.addWidget(self.tPushButton, 4, 2, 1, 1)
        self.lPushButton = QtGui.QPushButton(self.groupBox)
        self.lPushButton.setObjectName(_fromUtf8("lPushButton"))
        self.gridLayout.addWidget(self.lPushButton, 5, 0, 1, 2)
        self.zPushButton = QtGui.QPushButton(self.groupBox)
        self.zPushButton.setEnabled(False)
        self.zPushButton.setObjectName(_fromUtf8("zPushButton"))
        self.gridLayout.addWidget(self.zPushButton, 5, 2, 1, 1)
        self.cmdLineEdit = QtGui.QLineEdit(self.groupBox)
        self.cmdLineEdit.setObjectName(_fromUtf8("cmdLineEdit"))
        self.gridLayout.addWidget(self.cmdLineEdit, 6, 0, 1, 2)
        self.cmdSendPushButton = QtGui.QPushButton(self.groupBox)
        self.cmdSendPushButton.setObjectName(_fromUtf8("cmdSendPushButton"))
        self.gridLayout.addWidget(self.cmdSendPushButton, 6, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setAcceptDrops(False)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_3.setText(_translate("MainWindow", "Port", None))
        self.connectPushButton.setText(_translate("MainWindow", "Connect", None))
        self.label_2.setText(_translate("MainWindow", "Device", None))
        self.imageLabel.setText(_translate("MainWindow", "Image Preview", None))
        self.sendPushButton.setText(_translate("MainWindow", "Send to USB paper", None))
        self.saveXBMpushButton.setText(_translate("MainWindow", "Save image as XBM file", None))
        self.pushButtonAdd.setText(_translate("MainWindow", "Add file", None))
        self.pushButtonPaste.setText(_translate("MainWindow", "Paste", None))
        self.pushButtonRotate.setText(_translate("MainWindow", "Rotate", None))
        self.pushButtonPreview.setText(_translate("MainWindow", "Preview", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Image", None))
        self.groupBox.setTitle(_translate("MainWindow", "Debug", None))
        self.sectorLabel.setText(_translate("MainWindow", "Target Sector", None))
        self.randomPushButton.setText(_translate("MainWindow", "Random", None))
        self.qdPushButton.setText(_translate("MainWindow", "Quick Dump", None))
        self.dPushButton.setText(_translate("MainWindow", "Dump Sector", None))
        self.uPushButton.setText(_translate("MainWindow", "Upload Image", None))
        self.ePushButton.setText(_translate("MainWindow", "Erase Sector", None))
        self.wPushButton.setText(_translate("MainWindow", "Clear Screen", None))
        self.iPushButton.setText(_translate("MainWindow", "Show Image", None))
        self.fPushButton.setText(_translate("MainWindow", "Flash info", None))
        self.tPushButton.setText(_translate("MainWindow", "Temprature", None))
        self.lPushButton.setText(_translate("MainWindow", "List non-empty Sectors", None))
        self.zPushButton.setText(_translate("MainWindow", "Erase Chip", None))
        self.cmdSendPushButton.setText(_translate("MainWindow", "Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Advanced", None))

from graphicsscene import GraphicsView
