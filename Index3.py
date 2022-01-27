
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
editUI, _ = loadUiType(path.join(path.dirname(__file__), "Edit.ui"))


######################################### valditon and timer to label


class Main2(QMainWindow, editUI):


    global img
    img= "img/user-grean.png"
    global my_id
    my_id=15
    global new_data
    new_data="F@res"


    def __init__(self, parent=None):
        super(Main2, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        name=new_data

        self.set_data(name)

        ######## DB

        self.pushButton_1.clicked.connect(self.Edit_but)
        #self.pushButton_2.clicked.connect(self.exit_but)

        self.pushButton_3.clicked.connect(self.addimg)
        self.pushButton_4.clicked.connect(self.deleteimg)
        self.label_2.hide()

        

        #self.Login_But.clicked.connect(self.main_go)


    #def main_go(self):
     #   self.w = MM() 
        #self.w.setStyleSheet(style())
      #  self.w.show()
       # self.showMinimized()
        #print("hi11")
    def get_data(self,data):
        global new_data
        new_data=data
        return()



    def set_data(self,the_username):

        
        
        if(len(the_username) > 3):

            try:
                # connect to database
                db = sqlite3.connect("DB_app.db")
                print(" Connected to Database Successfully ")
                # setting up the cursor
                cr = db.cursor()
                find_user = ('SELECT * FROM user WHERE username = ? ')
                cr.execute(find_user,[(the_username)])
                result = cr.fetchone()
                #print(str(result))
                #k=str(result)
                global my_id
                my_id=result[0]

               
                #print(k.split(',')[1])
                self.lineEdit_2.setText(result[3])
                self.lineEdit_3.setText(result[4])
                self.lineEdit_4.setText(result[1])
                self.lineEdit_6.setText(result[2])
                self.lineEdit_7.setText(result[2])
                self.lineEdit_5.setText(result[5])

                imgs =result[6]
                #print(imgs)
                with open('img/new_img.png',"wb") as binary_image:
                    binary_code = binary_image.write(imgs)
                
                aa='img/new_img.png'
                dd=QPixmap(aa)
                self.labelimg.setPixmap(dd)
                global img
                img = aa
                self.label_2.hide()
              
            except sqlite3.Error as er:
                    print(f"Error Reading Date {er}")
                    self.label_2.setText(f"Error Reading Date {er}")
                    self.label_2.show()

            finally:
                if (db):
                    # I Add commit*
                    db.commit()
                    db.close()

            


    def Edit_but(self):

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
        msg="!"
        #x  = self.password_check(self,password)
        ######################

                    
        SpecialSym =['$', '@', '#', '%','+','-','*','/','!','^','!','&']
        val = True
        #msg=my_msg
        msg = "Password Edite successfully"
        if len(password) < 8:
            msg='length should be at least 8'
            val = False
            
        if len(password) > 20:
            msg='length should be not be greater than 20'
            val = False
            
        if not any(char.isdigit() for char in password):
            msg='Password should have at least one numeral'
            val = False
            
        if not any(char.isupper() for char in password):
            msg='Password should have at least one uppercase letter'
            val = False
            
        if not any(char.islower() for char in password):
            msg='Password should have at least one lowercase letter'
            val = False
            
        if not any(char in SpecialSym for char in password):
            msg='Password should have at least one of the symbols +-*/!^&$@#'
            val = False
        #if val:
        #    return val
        

        if(len(user_name) > 3):
            if(password == password_2 and val):
                    

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

                    #cr.execute(f"update User set(userName ,password,firstName ,lastName,email,img) values (?,?,?,?,?,?)",(user_name , password,first_name , last_name,Email,binary_code))
                    #cr.execute(f"insert into User(img) values(?),({binary_code})")
                    #cr.execute("insert into Account(userName ,password  ) values ('fares1' , '123f')")
                    global my_id
                    cr.execute(f"UPDATE User set userName =? ,password =?, firstName=? , lastName=?,email=?,img=? where user_id = ?",(user_name , password,first_name , last_name,Email,binary_code,my_id))
                                                    
                    
                    Notifier = ToastNotifier()
                    Notifier.show_toast(f" Prediction Mood!" , "you are Create a new account :"+user_name,
                    icon_path="img\Standar\mood_icon.ico" ,duration=5,threaded=True)
                    self.label_2.hide()
                  
                except sqlite3.Error as er:
                    print(f"Error Reading Date {er}")
                    self.label_2.setText(f"Error, {er}")
                    self.label_2.show()

                finally:
                    if (db):
                        # I Add commit*
                        db.commit()
                        db.close()

                        #self.lineEdit_2.setText(" ")
                        #self.lineEdit_3.setText(" ")
                        #self.lineEdit_4.setText(" ")
                        #self.lineEdit_5.setText(" ")
                        #self.lineEdit_6.setText(" ")
                        #self.lineEdit_7.setText(" ")


                        print(" Connected to Database is Closed ")

            else:
                self.label_2.setText(msg+"!")
                self.label_2.show()
        else:
                self.label_2.setText("UserName length should be at least 4!")
                self.label_2.show()


    
    #def exit_but(self):
        #app.exec_()
        #sys.exit(self.window)
    #    sys.exit("Thanks")

    def addimg(self):
        save_location = QFileDialog.getSaveFileName(self , caption="Save as" , directory="." , filter="All Files(*.*)")
        #print(save_location[0])
        global img
        img = save_location[0]
        #print(save_location)  2argumant
        #print(save_location[0]) 1argumant
        #print(str(save_location[0]))  1argumant-str
        self.label_2.hide()


        qpimg = QPixmap(str(save_location[0]))
        self.labelimg.setPixmap(qpimg)
    
    def deleteimg(self):
        a="img/user-grean.png"
        img = QPixmap(a)
        self.labelimg.setPixmap(img)

    ###############################################################################################


def main():
    app = QApplication(sys.argv)
    window = Main2()
    window.show()
    app.exec_()
    print("hi")


if __name__ == '__main__':
    main()

