# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 390)
        MainWindow.setMinimumSize(QSize(640, 390))
        MainWindow.setMaximumSize(QSize(640, 390))
        icon = QIcon()
        icon.addFile(u"image/login.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(168, 218, 220);")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelaccount = QLabel(self.centralwidget)
        self.labelaccount.setObjectName(u"labelaccount")
        self.labelaccount.setGeometry(QRect(-10, 0, 320, 390))
        self.labelaccount.setStyleSheet(u"\n"
"border-image: url(img/logo_mood.png);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 30, 281, 61))
        font = QFont()
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.PointingHandCursor))
        self.label.setStyleSheet(u" font-size:25px;\n"
" line-height:1.2;\n"
"  color: rgb(74, 74, 111);\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  padding: 0 20px;\n"
"  width: 100%;\n"
"  height: 50px;\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 100, 311, 281))
        self.label_2.setFont(font)
        self.label_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_2.setStyleSheet(u" font-size:25px;\n"
" line-height:1.2;\n"
"  color: rgb(74, 74, 111);\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  padding: 0 20px;\n"
"  width: 100%;\n"
"  height: 50px;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"about", None))
        self.labelaccount.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Priditon Of Mood", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PTUK \n"
"Fares kitani\n"
"2021-2022", None))
    # retranslateUi

