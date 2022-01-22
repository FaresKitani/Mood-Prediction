from keras.preprocessing.image import img_to_array
from keras.models import load_model

import cv2
import numpy as np
import sys



def Emotion_img(path):

    # parameters for loading data and images
    detection_model_path = r'C:\Users\hp\Downloads\Emotion_Detection_CNN-main\Emotion_Detection_CNN-main\haarcascade_frontalface_default.xml'
    emotion_model_path = r'C:\Users\hp\Downloads\Emotion_Detection_CNN-main\Emotion_Detection_CNN-main\model.h5'

    img_path = path

    # hyper-parameters for bounding boxes shape# models/_mini_XCEPTION.106-0.65.hdf5
    # loading models
    face_detection = cv2.CascadeClassifier(detection_model_path)
    emotion_classifier = load_model(emotion_model_path, compile=False)
    EMOTIONS = ["angry", "disgust", "scared", "happy", "sad", "surprised", "neutral"]

    # reading the frame
    orig_frame = cv2.imread(str(img_path))
    frame = cv2.imread(str(img_path), 0)
    faces = face_detection.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                            flags=cv2.CASCADE_SCALE_IMAGE)

    if len(faces) > 0:
        faces = sorted(faces, reverse=True, key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
        (fX, fY, fW, fH) = faces
        roi = frame[fY:fY + fH, fX:fX + fW]
        roi = cv2.resize(roi, (48, 48))
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)
        
        preds = emotion_classifier.predict(roi)[0]
        emotion_probability = np.max(preds)
        
        label = EMOTIONS[preds.argmax()]
        cv2.putText(orig_frame, label, (fX, fY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
        cv2.rectangle(orig_frame, (fX, fY), (fX + fW, fY + fH), (0, 0, 255), 2)


    cv2.imshow('test_face', orig_frame)

    #cv2.imwrite('test_output/' + img_path.split('/')[-1], orig_frame)
    cv2.imwrite('test_output/'+ img_path.split('/')[-1], orig_frame)

    newpath ='test_output/' + img_path.split('/')[-1]
    
   
    return(newpath )

        
    

    if (cv2.waitKey(9000) & 0xFF == ord('q')):
        sys.exit("Thanks")
    cv2.destroyAllWindows()
    

#Emotion_img('img/AC.jpeg')
#print(Emotion_img('aa.jpg'))
#img = "img/happy3.jpeg"
#A1 , A2 = Emotion_img(img)
#print(A1.split('/')[-1] + " \n" + A2)
