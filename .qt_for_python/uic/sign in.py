# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sign in.ui'
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
        MainWindow.resize(514, 592)
        MainWindow.setStyleSheet(u"QWidget\n"
"{\n"
"      color: rgb(74, 74, 111);\n"
"	  background-color: rgb(168, 218, 220);\n"
"    \n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 90, 131, 51))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 150, 151, 51))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 350, 161, 51))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 270, 151, 51))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 210, 151, 51))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 400, 151, 51))
        self.label_6.setFont(font)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(220, 100, 241, 51))
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(220, 160, 241, 51))
        self.textEdit_3 = QTextEdit(self.centralwidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(220, 220, 241, 51))
        self.textEdit_4 = QTextEdit(self.centralwidget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(220, 280, 241, 51))
        self.textEdit_5 = QTextEdit(self.centralwidget)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(220, 340, 241, 51))
        self.textEdit_6 = QTextEdit(self.centralwidget)
        self.textEdit_6.setObjectName(u"textEdit_6")
        self.textEdit_6.setGeometry(QRect(220, 400, 241, 51))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(420, 0, 91, 71))
        self.label_7.setFont(font)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(170, 20, 181, 61))
        self.label_8.setFont(font)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 121, 81))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"border-image: url(img/logo_mood.png);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(380, 490, 81, 51))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
" font: 10pt \"Microsoft Sans Serif\";\n"
" font-size:12px;\n"
" line-height:1.2;\n"
"  color: #f8f9fa;\n"
" text-transform:uppercase;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  padding: 0 20px;\n"
"  width: 100%;\n"
"  height: 50px;\n"
"  background-color: rgb(80, 80, 150);\n"
"  border-radius: 10px;\n"
"  box-shadow: 0 10px 30px 0px rgba(87, 184, 70, 0.5);\n"
"  transition: all 0.4s;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgb(74, 74, 125);\n"
"  box-shadow: 0 10px 30px 0px rgba(51, 51, 51, 0.5);\n"
" \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: rgb(74, 74, 111);\n"
"}")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(220, 490, 81, 51))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
" font: 10pt \"Microsoft Sans Serif\";\n"
" font-size:12px;\n"
" line-height:1.2;\n"
"  color: #f8f9fa;\n"
" text-transform:uppercase;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  padding: 0 20px;\n"
"  width: 100%;\n"
"  height: 50px;\n"
"  background-color: rgb(80, 80, 150);\n"
"  border-radius: 10px;\n"
"  box-shadow: 0 10px 30px 0px rgba(87, 184, 70, 0.5);\n"
"  transition: all 0.4s;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: rgb(74, 74, 125);\n"
"  box-shadow: 0 10px 30px 0px rgba(51, 51, 51, 0.5);\n"
" \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: rgb(74, 74, 111);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 514, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        self.label.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">First Name :</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("MainWindow", u"First Name :", None))
#if QT_CONFIG(whatsthis)
        self.label_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">First Name :</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Last Name :", None))
#if QT_CONFIG(whatsthis)
        self.label_3.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">First Name :</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"phone number\n"
"", None))
#if QT_CONFIG(whatsthis)
        self.label_4.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">First Name :</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Email :", None))
#if QT_CONFIG(whatsthis)
        self.label_5.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">First Name :</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"User name :", None))
#if QT_CONFIG(whatsthis)
        self.label_6.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">First Name :</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Age :", None))
#if QT_CONFIG(whatsthis)
        self.label_7.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">First Name :</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"sign in", None))
#if QT_CONFIG(whatsthis)
        self.label_8.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">First Name :</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Mood prediction\n"
"", None))
#if QT_CONFIG(whatsthis)
        self.label_9.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">First Name :</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_9.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ok", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

