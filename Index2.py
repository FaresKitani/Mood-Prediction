
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

# import for Viduo stream Emotion
from ViduoEmotion import EmotionStream

# import for DB_SQLite
import sqlite3

#notification 
from win10toast import ToastNotifier


#MainUI, _ = loadUiType(path.join(path.dirname(__file__), "Main_App_2.ui"))
#logUI, _ = loadUiType(path.join(path.dirname(__file__), "login.ui"))
sinUI, _ = loadUiType(path.join(path.dirname(__file__), "sing.ui"))


######################################### valditon and timer to label


class Main2(QMainWindow, sinUI):


    global img
    img= "img/user-grean.png"

    def __init__(self, parent=None):
        super(Main2, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

        ######## DB
        self.MyDB()

        self.pushButton_1.clicked.connect(self.save_but)
        self.pushButton_2.clicked.connect(self.exit_but)

        self.pushButton_3.clicked.connect(self.addimg)
        self.pushButton_4.clicked.connect(self.deleteimg)
        self.label_2.hide()

        

        #self.Login_But.clicked.connect(self.main_go)


    def main_go(self):
        self.w = MM() 
        #self.w.setStyleSheet(style())
        self.w.show()
        self.showMinimized()
        print("hi11")


    def save_but(self):

        first_name ="Fares"
        first_name = self.lineEdit_2.text()
        last_name= "kitani"
        last_name= self.lineEdit_3.text()
        image="img\happy2.jpeg"
        user_name= "User_f7"
        user_name = self.lineEdit_4.text()
        password="123"
        password = self.lineEdit_6.text()
        password_2="123"
        password_2 = self.lineEdit_7.text()
        Email="faris-yahoo.com"
        Email = self.lineEdit_5.text()

        global img
        image= img


        if(user_name != ""):
            if(password == password_2):
                    

                try:
                    # connect to database
                    db = sqlite3.connect("DB_app.db")
                    print(" Connected to Database Successfully ")
                    # setting up the cursor
                    cr = db.cursor()

                    

                    
                    


                    with open(image,"rb") as binary_image:
                        binary_code = binary_image.read()
                        #print(binary_code)
                    #cr.execute(" insert into student(name , img , user_id ) values(?, ? , ?)",('faris',binary_code, 1))

                    cr.execute(f"insert into User(userName ,password,firstName ,lastName,email,img) values (?,?,?,?,?,?)",(user_name , password,first_name , last_name,Email,binary_code))
                    #cr.execute(f"insert into User(img) values(?),({binary_code})")
                    #cr.execute("insert into Account(userName ,password  ) values ('fares1' , '123f')")

                    
                    Notifier = ToastNotifier()
                    Notifier.show_toast(f" Prediction Mood!" , "you are Create a new account :"+user_name,
                    icon_path="img\Standar\mood_icon.ico" ,duration=5,threaded=True)
                    
                    
                except sqlite3.Error as er:
                    print(f"Error Reading Date {er}")
                    self.label_2.setText(f"Error Reading Date {er}")
                    self.label_2.show()

                finally:
                    if (db):
                        # I Add commit*
                        db.commit()
                        db.close()

                        self.lineEdit_2.setText(" ")
                        self.lineEdit_3.setText(" ")
                        self.lineEdit_4.setText(" ")
                        self.lineEdit_5.setText(" ")
                        self.lineEdit_6.setText(" ")
                        self.lineEdit_7.setText(" ")


                        print(" Connected to Database is Closed ")

            else:
                self.label_2.setText("password !")
                self.label_2.show()
        else:
                self.label_2.setText("user name is empty !")
                self.label_2.show()


    
    def exit_but(self):


        sys.exit(self.window)
        #sys.exit("Thanks")

    def addimg(self):
        save_location = QFileDialog.getSaveFileName(self , caption="Save as" , directory="." , filter="All Files(*.*)")
        #print(save_location[0])
        global img
        img = save_location[0]
        #print(save_location)  2argumant
        #print(save_location[0]) 1argumant
        #print(str(save_location[0]))  1argumant-str

        qpimg = QPixmap(str(save_location[0]))
        self.labelimg.setPixmap(qpimg)
    
    def deleteimg(self):
        a=" "
        img = QPixmap(a)
        self.labelimg.setPixmap(img)







    ##############################################################################################
    ############# DB
    def MyDB(self):
        try:
            # connect to database
            db = sqlite3.connect("DB_app.db")
            print(" Connected to Database Successfully ")
            # setting up the cursor
            cr = db.cursor()

            cr.execute("create table if not exists User(user_id integer PRIMARY KEY AUTOINCREMENT,userName text UNIQUE,password text ,firstName text,lastName text,email text, img blob ) ")
            #cr.execute("create table if not exists Account( user_id integer, userName text ,password text  )")
            # now trying with one img Name chill1
            """""""""




            """""""""
        except sqlite3.Error as er:
            print("Error Reading Date {er}")

        finally:
            if (db):
                # I Add commit*
                db.commit()
                db.close()
                print(" Connected to Database is Closed ")





    ###############################################################################################


def main():
    app = QApplication(sys.argv)
    window = Main2()
    window.show()
    app.exec_()
    print("hi")


if __name__ == '__main__':
    main()

