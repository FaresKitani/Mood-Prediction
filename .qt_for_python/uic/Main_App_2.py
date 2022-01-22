# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_App_2.ui'
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
        MainWindow.resize(1278, 854)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setContextMenuPolicy(Qt.CustomContextMenu)
        MainWindow.setStyleSheet(u"QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"      color: rgb(74, 74, 111);\n"
"	  background-color: rgb(168, 218, 220);\n"
"    \n"
"}\n"
"\n"
"QTreeView, QListView\n"
"{\n"
"    background-color: silver;\n"
"    margin-left: 5px;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: #4A4A6F;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: #4A4A6F;\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
""
                        "        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #808080;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: #4A4A6F;\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 1px solid darkgray;*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: #4A4A6F;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"  "
                        "  border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    min-width: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: #4A4A6F;\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4A4A6F, stop: 1 #4A4A6F);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
""
                        "QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/dark_orange/img/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"    border: 1px solid darkgray;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"    border: 1px solid darkgray;\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 1px solid darkgray;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGrad"
                        "ient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScro"
                        "llBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
""
                        "      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    colo"
                        "r: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop"
                        ":0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/dark_orange/img/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar"
                        "\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
""
                        "    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
""
                        "        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/dark_orange/img/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #3A3939;\n"
"    height: 8px;\n"
"    background: #201F1F;\n"
"    margin: 2px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px "
                        "solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: -4px 0;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border: 1px solid #3A3939;\n"
"    width: 8px;\n"
"    background: #201F1F;\n"
"    margin: 0 0px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
"      stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
"    border: 1px solid #3A3939;\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    margin: 0 -4px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QAbstractSpinBox {\n"
"    padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"    border: 1px solid darkgray;\n"
"\n"
"    border-radius: 2px;\n"
"    min-width: 50px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ExiteButton = QPushButton(self.centralwidget)
        self.ExiteButton.setObjectName(u"ExiteButton")
        self.ExiteButton.setGeometry(QRect(1130, 750, 142, 45))
        self.ExiteButton.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
"}\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 50, 231, 61))
        self.label_Edit = QLabel(self.centralwidget)
        self.label_Edit.setObjectName(u"label_Edit")
        self.label_Edit.setGeometry(QRect(1120, 110, 161, 41))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_Edit.setFont(font1)
        self.label_Edit.setLayoutDirection(Qt.LeftToRight)
        self.label_Edit.setAlignment(Qt.AlignCenter)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(420, 560, 142, 45))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
"}\n"
"")
        self.deletButton = QPushButton(self.centralwidget)
        self.deletButton.setObjectName(u"deletButton")
        self.deletButton.setGeometry(QRect(620, 560, 142, 45))
        self.deletButton.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
        self.labelimg = QLabel(self.centralwidget)
        self.labelimg.setObjectName(u"labelimg")
        self.labelimg.setGeometry(QRect(390, 150, 400, 400))
        self.labelimg.setCursor(QCursor(Qt.PointingHandCursor))
        self.labelimg.setStyleSheet(u"image: url(img/Standar/Emoji_icon_without_Mouth.png);\n"
"\n"
"border: 4px solid #4A4A6F;\n"
"border-radius: 20px;\n"
" padding: 15px;")
        self.labelimg.setTextFormat(Qt.PlainText)
        self.labelimg.setScaledContents(True)
        self.labelimg.setMargin(10)
        self.labelimg2 = QLabel(self.centralwidget)
        self.labelimg2.setObjectName(u"labelimg2")
        self.labelimg2.setGeometry(QRect(840, 150, 400, 400))
        sizePolicy.setHeightForWidth(self.labelimg2.sizePolicy().hasHeightForWidth())
        self.labelimg2.setSizePolicy(sizePolicy)
        self.labelimg2.setCursor(QCursor(Qt.PointingHandCursor))
        self.labelimg2.setStyleSheet(u"image: url(img/Standar/Smiling_Emoji.png);\n"
"\n"
"\n"
"border: 4px solid #4A4A6F;\n"
"border-radius: 20px;\n"
"padding: 15px;")
        self.labelimg2.setTextFormat(Qt.PlainText)
        self.labelimg2.setScaledContents(True)
        self.labelimg2.setMargin(10)
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(650, 620, 151, 51))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(970, 80, 131, 51))
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(530, 80, 111, 51))
        self.predictButton = QPushButton(self.centralwidget)
        self.predictButton.setObjectName(u"predictButton")
        self.predictButton.setGeometry(QRect(930, 570, 201, 45))
        self.predictButton.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
"}\n"
"")
        self.ViduoButton = QPushButton(self.centralwidget)
        self.ViduoButton.setObjectName(u"ViduoButton")
        self.ViduoButton.setGeometry(QRect(220, 220, 142, 45))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ViduoButton.sizePolicy().hasHeightForWidth())
        self.ViduoButton.setSizePolicy(sizePolicy1)
        self.ViduoButton.setMinimumSize(QSize(142, 0))
        self.ViduoButton.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
#if QT_CONFIG(shortcut)
        self.ViduoButton.setShortcut(u"")
#endif // QT_CONFIG(shortcut)
        self.ViduoButton.setAutoDefault(False)
        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(10, 750, 201, 45))
        self.pushButton_9.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
"}\n"
"")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(800, 630, 451, 111))
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_13.setTextInteractionFlags(Qt.NoTextInteraction)
        self.ViduoButton_2 = QPushButton(self.centralwidget)
        self.ViduoButton_2.setObjectName(u"ViduoButton_2")
        self.ViduoButton_2.setGeometry(QRect(220, 160, 142, 45))
        self.ViduoButton_2.setMinimumSize(QSize(142, 0))
        self.ViduoButton_2.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(220, 690, 142, 45))
        self.pushButton_10.setMinimumSize(QSize(142, 0))
        self.pushButton_10.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
" \n"
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
        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(220, 630, 142, 45))
        self.pushButton_12.setMinimumSize(QSize(142, 0))
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(220, 750, 141, 45))
        self.comboBox.setStyleSheet(u"font: bold;\n"
" font-size:12px;\n"
"  color: #f8f9fa;\n"
" text-transform:uppercase;\n"
"  justify-content: center;\n"
"  align-items: center;\n"
"  padding: 0 10px;\n"
"  width: 100%;\n"
"  height: 50px;\n"
"  background-color: rgb(80, 80, 150);\n"
"  border-radius: 10px;")
        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(220, 450, 142, 45))
        self.pushButton_13.setMinimumSize(QSize(142, 0))
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(219, 400, 142, 45))
        self.pushButton_14.setMinimumSize(QSize(142, 0))
        self.pushButton_14.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
        self.pushButton_15 = QPushButton(self.centralwidget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(220, 510, 142, 45))
        self.pushButton_15.setMinimumSize(QSize(142, 0))
        self.pushButton_15.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
        self.pushButton_16 = QPushButton(self.centralwidget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(220, 570, 142, 45))
        self.pushButton_16.setMinimumSize(QSize(142, 0))
        self.pushButton_16.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 160, 201, 45))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
"   background-image: url(img/Standar/ddd1.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: left; \n"
"  \n"
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
"}\n"
"")
        self.pushButton.setIconSize(QSize(2, 2))
        self.pushButton.setAutoDefault(True)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 630, 201, 45))
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
"}\n"
"")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 400, 201, 45))
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
"}\n"
"")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 510, 201, 45))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
"}\n"
"")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(330, 510, 21, 21))
        self.label_5.setStyleSheet(u"image: url(img/Standar/NO_image.png);\n"
"  background-color: rgb(80, 80, 150);\n"
"")
        self.label_5.setScaledContents(True)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(330, 400, 21, 20))
        self.label_6.setStyleSheet(u"image: url(img/Standar/NO_image.png);\n"
"  background-color: rgb(80, 80, 150);\n"
"\n"
"")
        self.label_6.setScaledContents(True)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(330, 630, 21, 20))
        self.label_7.setStyleSheet(u"image: url(img/Standar/NO_image.png);\n"
"  background-color: rgb(80, 80, 150);\n"
"border-radius: 20px;\n"
"")
        self.label_7.setScaledContents(True)
        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(10, 280, 201, 45))
        self.pushButton_11.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
"}\n"
"")
        self.pushButton_17 = QPushButton(self.centralwidget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(220, 280, 142, 45))
        self.pushButton_17.setMinimumSize(QSize(142, 0))
        self.pushButton_17.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(330, 280, 21, 21))
        self.label_8.setStyleSheet(u"image: url(img/Standar/NO_image.png);\n"
"  background-color: rgb(80, 80, 150);\n"
"")
        self.label_8.setScaledContents(True)
        self.pushButton_18 = QPushButton(self.centralwidget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(220, 340, 142, 45))
        self.pushButton_18.setMinimumSize(QSize(142, 0))
        self.pushButton_18.setStyleSheet(u"QPushButton {\n"
" font: bold;\n"
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
        self.pushButton_Edit = QPushButton(self.centralwidget)
        self.pushButton_Edit.setObjectName(u"pushButton_Edit")
        self.pushButton_Edit.setGeometry(QRect(1150, 0, 111, 111))
        self.pushButton_Edit.setStyleSheet(u"QPushButton {\n"
"\n"
"  box-shadow: 0 10px 30px 0px rgba(87, 184, 70, 0.5);\n"
"  transition: all 0.4s;\n"
"image: url(img/user-grean.png);\n"
"background-color: rgb(168, 218, 220);\n"
"border: 4px solid #4A4A6F;\n"
"border-radius: 20px;\n"
" padding: 8px;\n"
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
"}\n"
"")
        self.pushButton_Edit.setAutoDefault(True)
        self.pushButton_Edit.setFlat(True)
        self.pushButton_Edit_2 = QPushButton(self.centralwidget)
        self.pushButton_Edit_2.setObjectName(u"pushButton_Edit_2")
        self.pushButton_Edit_2.setGeometry(QRect(10, 0, 111, 111))
        self.pushButton_Edit_2.setStyleSheet(u"\n"
"QPushButton {\n"
"\n"
"  box-shadow: 0 10px 30px 0px rgba(87, 184, 70, 0.5);\n"
"  transition: all 0.4s;\n"
"image: url(img/logo_Mood.png);\n"
"background-color: rgb(168, 218, 220);\n"
"border: 4px solid #4A4A6F;\n"
"border-radius: 20px;\n"
" padding: 8px;\n"
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
"}\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1278, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ExiteButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Mood Prediction </span></p></body></html>", None))
        self.label_Edit.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">User Name</span></p></body></html>", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
#if QT_CONFIG(whatsthis)
        self.deletButton.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">+</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.deletButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.labelimg.setText("")
        self.labelimg2.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Mood :</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Prediction :</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Normal :</span></p></body></html>", None))
        self.predictButton.setText(QCoreApplication.translate("MainWindow", u"Prediction", None))
        self.ViduoButton.setText(QCoreApplication.translate("MainWindow", u"multi-face\n"
"", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_9.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">+</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"left\">Happy </p></body></html>", None))
        self.ViduoButton_2.setText(QCoreApplication.translate("MainWindow", u" single face\n"
"", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_10.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">+</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"prediction ", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_12.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">+</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Mood !", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Sad", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Happy", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Neutral", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Disgusted", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Angry", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Fearful", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Surprised", None))

#if QT_CONFIG(whatsthis)
        self.comboBox.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p ><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
        self.pushButton_13.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">+</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"prediction ", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_14.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">+</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_15.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">+</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_16.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">+</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"prediction ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Live Video Streaming", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"predict Notification", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"predict  Video", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"predict folder", None))
        self.label_5.setText("")
        self.label_6.setText("")
        self.label_7.setText("")
#if QT_CONFIG(whatsthis)
        self.pushButton_11.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">+</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"predict and print", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_17.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">+</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.label_8.setText("")
#if QT_CONFIG(whatsthis)
        self.pushButton_18.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">+</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"prediction ", None))
        self.pushButton_Edit.setText("")
        self.pushButton_Edit_2.setText("")
    # retranslateUi

