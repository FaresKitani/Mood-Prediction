
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

#notification 
from win10toast import ToastNotifier

# import for Viduo stream Emotion
from ViduoEmotion import EmotionStream

# import for DB_SQLite
import sqlite3

#imp
from Index1 import Main as MM

from Index2 import Main2 as MS
from Index3 import Main2 as SS

#MainUI, _ = loadUiType(path.join(path.dirname(__file__), "Main_App_2.ui"))
logUI, _ = loadUiType(path.join(path.dirname(__file__), "login.ui"))
#sinUI, _ = loadUiType(path.join(path.dirname(__file__), "SignIn.ui"))


class Main(QMainWindow, logUI):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Login_But.clicked.connect(self.main_go)
        self.signin_But.clicked.connect(self.sing_go)

        global my_ID
        my_ID=0
        global my_user_name
        my_user_name=" "
        global my_password 
        my_password=" "


        #################### hide label
        self.label_2.hide()
        self.label_3.hide()



    def main_go(self):

        the_username = self.user_text.text()
        the_password = self.password_text.text()

        

        


        ############################## user name where the_userName = \'{user}\'  

        try:
            # connect to database
            db = sqlite3.connect("DB_app.db")
            print(" Connected to Database Successfully ")
            # setting up the cursor
            cr = db.cursor()
            #cr.execute('SELECT userName,password FROM User ')

            #the_User= cr.fetchall()

            #cr.execute("create table if not exists User(user_id integer PRIMARY KEY AUTOINCREMENT,userName text UNIQUE,password text ,firstName text,lastName text,email text, img blob ) ")
 

            find_user = ('SELECT userName,password FROM user WHERE username = ? and password = ?')
            cr.execute(find_user,[(the_username),(the_password)])
            result = cr.fetchall()
            if result:
                global my_ID
                my_ID=0
                global my_user_name
                my_user_name= the_username
                global my_password 
                my_password= the_password
                

                self.w = MM()
                ################################ send img and username to index1
                
                self.w.fun_Edit(my_user_name)
                ###################################### end send
                self.ss1 = SS()
                self.ss1.set_data(my_user_name)
                #self.ss1.get_data(my_user_name)
                #self.w.setStyleSheet(style())
                self.w.show()
                self.showMinimized()

                Notifier = ToastNotifier()
                Notifier.show_toast(" Prediction Mood!" , " logiN in your account ",
                icon_path="img\Standar\mood_icon.ico" ,duration=5,threaded=True)
                
                self.label_2.hide()

                print("hi11")
            else:
                Notifier = ToastNotifier()
                Notifier.show_toast(" Prediction Mood!" , " Oops! ,Username Not Found. ",
                icon_path="img\Standar\mood_icon.ico" ,duration=5,threaded=True)
                self.label_2.show()

        except sqlite3.Error as er:
            print("Error Reading Date {er}")

        finally:
            if (db):
                # I Add commit*
                db.commit()
                db.close()
                print(" Connected to Database is Closed ")





    ##############################################################################################


    def sing_go(self):

        Notifier = ToastNotifier()
        Notifier.show_toast(" Prediction Mood!" , " Create a new account ",
        icon_path="img\Standar\mood_icon.ico" ,duration=5,threaded=True)

        self.w2 = MS() 
        #self.w.setStyleSheet(style())
        self.w2.show()
        self.showMinimized()

        self.label_2.hide()

        print("hi11")
    


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()
    print("hi")


if __name__ == '__main__':
    main()

