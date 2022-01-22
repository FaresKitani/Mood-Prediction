#connetion with DB

#connetion with QT_Disinger

#Start codeing


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
from Mood_imgs import EmotionStream_one_face
from Emotion import Emotion_img
from TestEmotionDetector import TestEmotion
from Emotion_print import print_Emotion

# import for DB_SQLite
import sqlite3

#import Edit UI
from Index3 import Main2 as Edit_UI



MainUI, _ = loadUiType(path.join(path.dirname(__file__), "Main_App_2.ui"))
logUI,_ =loadUiType(path.join(path.dirname(__file__),"login.ui"))

class Main(QMainWindow, MainUI):

    
    path_img ='img/happy2.jpeg'
    global img
    global img_video
    global img_print

    img = "AC.jpeg" 

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

        
        
        

        #hidden button  
        self.ViduoButton_2.hide()
        self.ViduoButton.hide()

        self.comboBox.hide()
        self.pushButton_12.hide()
        self.pushButton_10.hide()
        self.label_7.hide()

        self.pushButton_14.hide()
        self.pushButton_13.hide()
        self.label_6.hide()

        self.pushButton_15.hide()
        self.pushButton_16.hide()
        self.label_5.hide()

        self.pushButton_17.hide()
        self.pushButton_18.hide()
        self.label_8.hide()

        #############################################

        print("constractor")    
        self.pushButton_4.clicked.connect(self.addimg)
        self.ExiteButton.clicked.connect(self.exit_but)
        self.deletButton.clicked.connect(self.delet_but)
        self.predictButton.clicked.connect(self.prediction_but)
        self.ViduoButton.clicked.connect(self.startViduo_but)
        self.ViduoButton_2.clicked.connect(self.startViduoOneFace_but)
        ####hide and show
        self.pushButton.clicked.connect(self.hidStream1)
        self.pushButton_2.clicked.connect(self.hidStream2)
        self.pushButton_3.clicked.connect(self.hidStream3)
        self.pushButton_5.clicked.connect(self.hidStream4)
        self.pushButton_11.clicked.connect(self.hidStream5)
        ## added

        self.pushButton_14.clicked.connect(self.video_add)
        self.pushButton_17.clicked.connect(self.print_add)
        self.pushButton_15.clicked.connect(self.folder_add)
        self.pushButton_12.clicked.connect(self.Notification_add)

        ################# pridict
        self.pushButton_13.clicked.connect(self.video_pridict)
        self.pushButton_18.clicked.connect(self.print_pridict)
        self.pushButton_16.clicked.connect(self.folder_pridict)
        self.pushButton_10.clicked.connect(self.Notification_pridict)


        ##################### Creat Edit UI
        self.pushButton_Edit.clicked.connect(self.Create_Edit)


            
        #fimg = QPixmap('img\F3.jpeg')
        #self.labelimg2.setPixmap(fimg)

    def exit_but(self):
       if (ord('q')):
            sys.exit("Thanks")

    def delet_but(self):
        L1 =QPixmap('img\Standar\Emoji_icon_without_Mouth.png')
        L2 =QPixmap('img\Standar\Smiling_Emoji.png')

        
        self.labelimg.setPixmap(L1)
        self.labelimg2.setPixmap(L2)

    def prediction_but(self):
        
        global img

        #img =self.labelimg.getPixmap
        try:
            path_didiction, mood_didiction = TestEmotion(img)
            print(path_didiction)
            A2=str(mood_didiction)
            A1 =QPixmap(path_didiction)
            self.label_13.setText(A2)
            self.labelimg2.setPixmap(A1)
            #print(A1)
        except:
            self.label_13.setText(" Oops! , don't can pridict this image.")
        

        

    def startViduo_but(self):
        EmotionStream()

    def startViduoOneFace_but(self):
        EmotionStream_one_face()

    def about_but(self):
        pass
        ################ Adding image

    def addimg(self):
        save_location = QFileDialog.getSaveFileName(self , caption="Save as" , directory="." , filter="All Files(*.*)")
        #print(save_location[0])

        qpimg = QPixmap(str(save_location[0]))
        self.labelimg.setPixmap(qpimg)
        global img
        img = save_location[0]
        #Main.MyDB(self)

    def video_add(self):
        save_location = QFileDialog.getSaveFileName(self , caption="Save as" , directory="." , filter="All Files(*.*)")
        #print(save_location[0])

        qpimg = QPixmap(str(save_location[0]))
        self.labelimg.setPixmap(qpimg)
        global img_video
        img_video = save_location[0]

        if(img_video):
            yas_img = "img\Standar\yes_img.png"
            self.label_6.setPixmap(QPixmap(yas_img))

    def print_add(self):
        save_location = QFileDialog.getSaveFileName(self , caption="Save as" , directory="." , filter="All Files(*.*)")
        #print(save_location[0])

        qpimg = QPixmap(str(save_location[0]))
        self.labelimg.setPixmap(qpimg)
        global img_print
        img_print = save_location[0]

        yas_img = "img\Standar\yes_img.png"
        self.label_8.setPixmap(QPixmap(yas_img))

    def folder_add(self):
        save_location = QFileDialog.getSaveFileName(self , caption="Save as" , directory="." , filter="All Files(*.*)")
        #print(save_location[0])

        qpimg = QPixmap(str(save_location[0]))
        self.labelimg.setPixmap(qpimg)
        global img
        img = save_location[0]

        yas_img = "img\Standar\yes_img.png"
        self.label_5.setPixmap(QPixmap(yas_img))

    def Notification_add(self):
        save_location = QFileDialog.getSaveFileName(self , caption="Save as" , directory="." , filter="All Files(*.*)")
        #print(save_location[0])

        qpimg = QPixmap(str(save_location[0]))
        self.labelimg.setPixmap(qpimg)
        global img
        img = save_location[0]

        yas_img = "img\Standar\yes_img.png"
        self.label_7.setPixmap(QPixmap(yas_img))
    
    ################################################ 

    ############################################### pridict

    def video_pridict(self):
        global img_video
        TestEmotion(img_video)
        #img_video = ""
        
        No_img = "img\Standar\no_image.png"
        self.label_6.setPixmap(QPixmap(No_img))

    def print_pridict(self):

        global img_print
        print_Emotion(img_print)

        No_img = "img\Standar\no_image.png"
        self.label_8.setPixmap(QPixmap(No_img))

        Notifier = ToastNotifier()
        Notifier.show_toast(" Prediction Mood!" , " The Prediction and print image is done. ",
        icon_path="img\Standar\mood_icon.ico" ,duration=5,threaded=True)
        
    def folder_pridict(self):
        pass

    
    def Notification_pridict(self):
        pass






    

    def Create_Edit(self):

        Notifier = ToastNotifier()
        Notifier.show_toast(" Prediction Mood!" , " You can Edit your account ",
        icon_path="img\Standar\mood_icon.ico" ,duration=5,threaded=True)

        self.w2 = Edit_UI() 
        #self.w.setStyleSheet(style())
        self.w2.show()
        self.showMinimized()
        print("Edit Ui")

    def fun_Edit(self,my_user_name):
        t1 = my_user_name
        self.label_Edit.setText(t1)
        try:
            # connect to database
            db = sqlite3.connect("DB_app.db")
            print(" Connected to Database Successfully ")
            # setting up the cursor
            cr = db.cursor()
            find_user = ('SELECT * FROM user WHERE username = ? ')
            cr.execute(find_user,[(t1)])
            result = cr.fetchone()
            myimg=result[6]
            with open('img/new1_img.png',"wb") as binary_image:
                    binary_code = binary_image.write(myimg)
            aa='img/new1_img.png'
            self.pushButton_Edit.setStyleSheet("border-image : url(img/new1_img.png);background-color: rgb(168, 218, 220);border: 4px solid #4A4A6F;border-radius: 20px;padding: 8px;")
       
        
        except:
                print(f"Error Reading Date ")

        




    ###################################################################

    ############################################ hide and show
    hidden1 = True

    def hidStream1(self):
        if self.hidden1:
            self.ViduoButton_2.show()
            self.ViduoButton.show()
            self.hidden1 = False
        else:
            self.ViduoButton_2.hide()
            self.ViduoButton.hide()
            self.hidden1 = True


    hidden2 = True

    def hidStream2(self):
        if self.hidden2:
            self.comboBox.show()
            self.pushButton_12.show()
            self.pushButton_10.show()
            self.label_7.show()

            self.hidden2 = False
        else:
            self.comboBox.hide()
            self.pushButton_12.hide()
            self.pushButton_10.hide()
            self.label_7.hide()
            self.hidden2 = True

    hidden3 = True

    def hidStream3(self):
        if self.hidden3:
            self.pushButton_14.show()
            self.pushButton_13.show()
            self.label_6.show()
            self.hidden3 = False
        else:
            self.pushButton_14.hide()
            self.pushButton_13.hide()
            self.label_6.hide()
            self.hidden3 = True


    hidden4 = True

    def hidStream4(self):
        if self.hidden4:
            self.pushButton_15.show()
            self.pushButton_16.show()
            self.label_5.show()
            self.hidden4 = False
        else:
            self.pushButton_15.hide()
            self.pushButton_16.hide()
            self.label_5.hide()
            self.hidden4 = True

    hidden5 = True

    def hidStream5(self):
        if self.hidden5:
            self.pushButton_17.show()
            self.pushButton_18.show()
            self.label_8.show()
            self.hidden5 = False
        else:
            self.pushButton_17.hide()
            self.pushButton_18.hide()
            self.label_8.hide()
            self.hidden5 = True


    ############################################









    def MyDB(self):
        try:
            # connect to database
            db = sqlite3.connect("DB_app.db")
            print(" Connected to Database Successfully ")
            # setting up the cursor
            cr = db.cursor()

            
        except sqlite3.Error as er:
            print("Error Reading Date {er}")

        finally:
            if (db):
                # I Add commit*
                db.commit()
                db.close()
                print(" Connected to Database is Closed ")


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()
    print("hi")


if __name__ == '__main__':
    main()


