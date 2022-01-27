
# import for QT5 & QT_designer

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#from PyQt5.QtGui import QPixmap
from PyQt5.QtDesigner import *




from PyQt5.uic import loadUiType

import sys
import os

# import for conniction betwean pycharm and QT_designer
from os import path

aboutUI,_ =loadUiType(path.join(path.dirname(__file__),"about.ui"))



class Main(QMainWindow, aboutUI):
    
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()
    print("hi")


if __name__ == '__main__':
    main()


