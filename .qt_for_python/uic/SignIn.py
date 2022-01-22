# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SignIn.ui'
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
        MainWindow.resize(454, 606)
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
        self.label_3.setGeometry(QRect(30, 330, 141, 61))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 280, 151, 51))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 210, 151, 51))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 390, 151, 51))
        self.label_6.setFont(font)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(200, 20, 191, 61))
        self.label_8.setFont(font)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 161, 91))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"border-image: url(img/logo_mood.png);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(340, 490, 81, 51))
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
"\n"
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
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 490, 81, 51))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
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
"  background-color: rgb(110, 20, 20);\n"
"  border-radius: 10px;\n"
"  box-shadow: 0 10px 30px 0px rgba(87, 184, 70, 0.5);\n"
"  transition: all 0.4s;\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(74, 20, 20);\n"
"  box-shadow: 0 10px 30px 0px rgba(51, 51, 51, 0.5);\n"
" \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(110, 20, 20);\n"
"}")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(190, 280, 231, 41))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	background-image: url();\n"
"    background-repeat: no-repeat;\n"
"    background-position: left;\n"
"    color: rgb(74, 74, 111);\n"
"	font-family:'Poppins-Medium', sans-serif;\n"
"    font-size: 18px;\n"
"    padding: 4 4 4 35; /* left padding (last number) must be more than the icon's width */\n"
"	border-radius:10px;\n"
"	border-bottom:2px solid #d9d9d9;\n"
"	background-color: rgb(241, 250, 238);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(241, 250, 238);\n"
"}")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(190, 100, 231, 41))
        font1 = QFont()
        font1.setFamily(u"Poppins-Medium,sans-serif")
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"	background-image: url();\n"
"    background-repeat: no-repeat;\n"
"    background-position: left;\n"
"    color: rgb(74, 74, 111);\n"
"	font-family:'Poppins-Medium', sans-serif;\n"
"    font-size: 18px;\n"
"    padding: 4 4 4 35; /* left padding (last number) must be more than the icon's width */\n"
"	border-radius:10px;\n"
"	border-bottom:2px solid #d9d9d9;\n"
"	background-color: rgb(241, 250, 238);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(241, 250, 238);\n"
"}")
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(190, 160, 231, 41))
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"	background-image: url();\n"
"    background-repeat: no-repeat;\n"
"    background-position: left;\n"
"    color: rgb(74, 74, 111);\n"
"	font-family:'Poppins-Medium', sans-serif;\n"
"    font-size: 18px;\n"
"    padding: 4 4 4 35; /* left padding (last number) must be more than the icon's width */\n"
"	border-radius:10px;\n"
"	border-bottom:2px solid #d9d9d9;\n"
"	background-color: rgb(241, 250, 238);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(241, 250, 238);\n"
"}")
        self.lineEdit_4 = QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(190, 220, 231, 41))
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"	background-image: url();\n"
"    background-repeat: no-repeat;\n"
"    background-position: left;\n"
"    color: rgb(74, 74, 111);\n"
"	font-family:'Poppins-Medium', sans-serif;\n"
"     font-size: 18px;\n"
"    padding: 4 4 4 35; /* left padding (last number) must be more than the icon's width */\n"
"	border-radius:10px;\n"
"	border-bottom:2px solid #d9d9d9;\n"
"	background-color: rgb(241, 250, 238);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(241, 250, 238);\n"
"}")
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(190, 340, 231, 41))
        self.lineEdit_5.setStyleSheet(u"QLineEdit{\n"
"	background-image: url();\n"
"    background-repeat: no-repeat;\n"
"    background-position: left;\n"
"    color: rgb(74, 74, 111);\n"
"	font-family:'Poppins-Medium', sans-serif;\n"
"    font-size: 18px;\n"
"    padding: 4 4 4 35; /* left padding (last number) must be more than the icon's width */\n"
"	border-radius:10px;\n"
"	border-bottom:2px solid #d9d9d9;\n"
"	background-color: rgb(241, 250, 238);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(241, 250, 238);\n"
"}")
        self.lineEdit_6 = QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(190, 400, 231, 41))
        self.lineEdit_6.setStyleSheet(u"QLineEdit{\n"
"	background-image: url();\n"
"    background-repeat: no-repeat;\n"
"    background-position: left;\n"
"    color: rgb(74, 74, 111);\n"
"	font-family:'Poppins-Medium', sans-serif;\n"
"    font-size: 18px;\n"
"    padding: 4 4 4 35; /* left padding (last number) must be more than the icon's width */\n"
"	border-radius:10px;\n"
"	border-bottom:2px solid #d9d9d9;\n"
"	background-color: rgb(241, 250, 238);\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(241, 250, 238);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 454, 26))
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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Paswward :", None))
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
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Paswward2 :", None))
#if QT_CONFIG(whatsthis)
        self.label_8.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">First Name :</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u" Prediction Mood\n"
"", None))
#if QT_CONFIG(whatsthis)
        self.label_9.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">First Name :</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_9.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Exite", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paswward", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paswward", None))
    # retranslateUi

