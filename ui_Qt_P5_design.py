# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qt_P5_design.ui',
# licensing of 'Qt_P5_design.ui' applies.
#
# Created: Thu Jul 18 15:25:06 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 892)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.videoScreen = QVideoWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoScreen.sizePolicy().hasHeightForWidth())
        self.videoScreen.setSizePolicy(sizePolicy)
        self.videoScreen.setObjectName("videoScreen")
        self.verticalLayout_2.addWidget(self.videoScreen)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 8, -1, 8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbTimeReal = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbTimeReal.setFont(font)
        self.lbTimeReal.setObjectName("lbTimeReal")
        self.horizontalLayout_2.addWidget(self.lbTimeReal)
        self.slTimeBarre = QtWidgets.QSlider(self.centralwidget)
        self.slTimeBarre.setMinimumSize(QtCore.QSize(20, 30))
        self.slTimeBarre.setOrientation(QtCore.Qt.Horizontal)
        self.slTimeBarre.setObjectName("slTimeBarre")
        self.horizontalLayout_2.addWidget(self.slTimeBarre)
        self.lbTimeTot = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbTimeTot.setFont(font)
        self.lbTimeTot.setObjectName("lbTimeTot")
        self.horizontalLayout_2.addWidget(self.lbTimeTot)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbLect = QtWidgets.QPushButton(self.centralwidget)
        self.pbLect.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbLect.setFont(font)
        self.pbLect.setObjectName("pbLect")
        self.horizontalLayout.addWidget(self.pbLect)
        self.pbPause = QtWidgets.QPushButton(self.centralwidget)
        self.pbPause.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbPause.setFont(font)
        self.pbPause.setObjectName("pbPause")
        self.horizontalLayout.addWidget(self.pbPause)
        self.pbStop = QtWidgets.QPushButton(self.centralwidget)
        self.pbStop.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbStop.setFont(font)
        self.pbStop.setObjectName("pbStop")
        self.horizontalLayout.addWidget(self.pbStop)
        self.pbPreced = QtWidgets.QPushButton(self.centralwidget)
        self.pbPreced.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbPreced.setFont(font)
        self.pbPreced.setObjectName("pbPreced")
        self.horizontalLayout.addWidget(self.pbPreced)
        self.pbSuiv = QtWidgets.QPushButton(self.centralwidget)
        self.pbSuiv.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pbSuiv.setFont(font)
        self.pbSuiv.setObjectName("pbSuiv")
        self.horizontalLayout.addWidget(self.pbSuiv)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        spacerItem = QtWidgets.QSpacerItem(20, 85, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbListFilm = QtWidgets.QLabel(self.centralwidget)
        self.lbListFilm.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbListFilm.setFont(font)
        self.lbListFilm.setObjectName("lbListFilm")
        self.verticalLayout_3.addWidget(self.lbListFilm)
        self.listFilm = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listFilm.sizePolicy().hasHeightForWidth())
        self.listFilm.setSizePolicy(sizePolicy)
        self.listFilm.setObjectName("listFilm")
        self.verticalLayout_3.addWidget(self.listFilm)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pbAjout = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbAjout.setFont(font)
        self.pbAjout.setObjectName("pbAjout")
        self.horizontalLayout_4.addWidget(self.pbAjout)
        self.pbSuppr = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbSuppr.setFont(font)
        self.pbSuppr.setObjectName("pbSuppr")
        self.horizontalLayout_4.addWidget(self.pbSuppr)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbVolumeTitre = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbVolumeTitre.setFont(font)
        self.lbVolumeTitre.setAlignment(QtCore.Qt.AlignCenter)
        self.lbVolumeTitre.setObjectName("lbVolumeTitre")
        self.horizontalLayout_3.addWidget(self.lbVolumeTitre)
        self.dlVolume = QtWidgets.QDial(self.centralwidget)
        self.dlVolume.setMaximumSize(QtCore.QSize(50, 50))
        self.dlVolume.setObjectName("dlVolume")
        self.horizontalLayout_3.addWidget(self.dlVolume)
        self.lbVolumePourc = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lbVolumePourc.setFont(font)
        self.lbVolumePourc.setAlignment(QtCore.Qt.AlignCenter)
        self.lbVolumePourc.setObjectName("lbVolumePourc")
        self.horizontalLayout_3.addWidget(self.lbVolumePourc)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.lbTimeReal.setText(QtWidgets.QApplication.translate("MainWindow", "00:00:00", None, -1))
        self.lbTimeTot.setText(QtWidgets.QApplication.translate("MainWindow", "00:00:00", None, -1))
        self.pbLect.setText(QtWidgets.QApplication.translate("MainWindow", "Lecture", None, -1))
        self.pbPause.setText(QtWidgets.QApplication.translate("MainWindow", "Pause", None, -1))
        self.pbStop.setText(QtWidgets.QApplication.translate("MainWindow", "Stop", None, -1))
        self.pbPreced.setText(QtWidgets.QApplication.translate("MainWindow", "Précédent", None, -1))
        self.pbSuiv.setText(QtWidgets.QApplication.translate("MainWindow", "Suivant", None, -1))
        self.lbListFilm.setText(QtWidgets.QApplication.translate("MainWindow", "Liste de lecture :", None, -1))
        self.pbAjout.setText(QtWidgets.QApplication.translate("MainWindow", "+", None, -1))
        self.pbSuppr.setText(QtWidgets.QApplication.translate("MainWindow", "-", None, -1))
        self.lbVolumeTitre.setText(QtWidgets.QApplication.translate("MainWindow", "Volume :", None, -1))
        self.lbVolumePourc.setText(QtWidgets.QApplication.translate("MainWindow", "0%", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "Fichier", None, -1))
        self.menuAide.setTitle(QtWidgets.QApplication.translate("MainWindow", "Aide", None, -1))

from PySide2.QtMultimediaWidgets import QVideoWidget
