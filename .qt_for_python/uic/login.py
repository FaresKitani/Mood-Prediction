# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
        MainWindow.setStyleSheet(u"QWidget\n"
"{\n"
"      color: rgb(74, 74, 111);\n"
"	  background-color: rgb(168, 218, 220);\n"
"    \n"
"}\n"
"QPushButton {\n"
" font: bold;\n"
" font-size:12px;\n"
" line-height:1.2;\n"
"  color: #f8f9fa;\n"
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
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.user_text = QLineEdit(self.centralwidget)
        self.user_text.setObjectName(u"user_text")
        self.user_text.setEnabled(True)
        self.user_text.setGeometry(QRect(370, 120, 211, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_text.sizePolicy().hasHeightForWidth())
        self.user_text.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Poppins-Medium,sans-serif")
        self.user_text.setFont(font)
        self.user_text.setTabletTracking(False)
        self.user_text.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.user_text.setAcceptDrops(True)
        self.user_text.setAutoFillBackground(False)
        self.user_text.setStyleSheet(u"QLineEdit{\n"
"	background-image: url(img/Standar/user.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: left;\n"
"    color: rgb(74, 74, 111);\n"
"	font-family:'Poppins-Medium', sans-serif;\n"
"    font-size: 12px;\n"
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
        self.user_text.setFrame(False)
        self.user_text.setDragEnabled(False)
        self.user_text.setReadOnly(False)
        self.user_text.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.user_text.setClearButtonEnabled(True)
        self.password_text = QLineEdit(self.centralwidget)
        self.password_text.setObjectName(u"password_text")
        self.password_text.setEnabled(True)
        self.password_text.setGeometry(QRect(370, 190, 211, 31))
        self.password_text.setFont(font)
        self.password_text.setAutoFillBackground(False)
        self.password_text.setStyleSheet(u"QLineEdit {\n"
"	background-image: url(img/Standar/password.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: left;\n"
"   color: rgb(74, 74, 111);\n"
"	font-family:'Poppins-Medium', sans-serif;\n"
"    font-size: 12px;\n"
"    padding: 4 4 4 35; /* left padding (last number) must be more than the icon's width */\n"
"	border-radius: 10px;\n"
"	border-bottom:2px solid #d9d9d9;\n"
"	background-color: rgb(241, 250, 238);\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    border: 2px solid rgb(48, 50, 62);\n"
"}\n"
"QLineEdit:focus{\n"
"    border: 2px solid rgb(85, 170, 255);\n"
"    background-color: rgb(241, 250, 238);\n"
"}")
        self.password_text.setEchoMode(QLineEdit.Password)
        self.password_text.setReadOnly(False)
        self.password_text.setClearButtonEnabled(True)
        self.Login_But = QPushButton(self.centralwidget)
        self.Login_But.setObjectName(u"Login_But")
        self.Login_But.setGeometry(QRect(400, 260, 141, 25))
        self.Login_But.setStyleSheet(u"")
        self.Login_But.setCheckable(False)
        self.Login_But.setChecked(False)
        self.Login_But.setAutoRepeat(False)
        self.Login_But.setAutoExclusive(False)
        self.labelaccount = QLabel(self.centralwidget)
        self.labelaccount.setObjectName(u"labelaccount")
        self.labelaccount.setGeometry(QRect(-10, 0, 320, 390))
        self.labelaccount.setStyleSheet(u"\n"
"border-image: url(img/logo_mood.png);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 40, 281, 51))
        font1 = QFont()
        self.label.setFont(font1)
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
        self.signin_But = QPushButton(self.centralwidget)
        self.signin_But.setObjectName(u"signin_But")
        self.signin_But.setGeometry(QRect(400, 310, 141, 25))
        self.signin_But.setStyleSheet(u"")
        self.signin_But.setCheckable(False)
        self.signin_But.setChecked(False)
        self.signin_But.setAutoRepeat(False)
        self.signin_But.setAutoExclusive(False)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(380, 160, 201, 20))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:rgb(222, 62, 8);\n"
"font-family:'Poppins-Medium', sans-serif;\n"
"font-size: 14px;")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(440, 230, 55, 16))
        self.label_3.setStyleSheet(u"color:rgb(222, 62, 8);\n"
"font-family:'Poppins-Medium', sans-serif;\n"
"font-size: 13px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login", None))
#if QT_CONFIG(whatsthis)
        self.user_text.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.user_text.setText("")
        self.user_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u" User Name", None))
        self.password_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Password", None))
        self.Login_But.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.labelaccount.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Mood Prediction\n"
"", None))
        self.signin_But.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Oops! ,Username Not Found.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

