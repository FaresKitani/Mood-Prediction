import os


print("1")
#os.startfile('C:\FARES-Lenove\Cooding\Main project/predict_data')

folder_path = r'C:\\FARES-Lenove\\Cooding\\Main project\\predict_data'
fileNames = os.listdir(folder_path)
for fileName in fileNames:

    print("2")

    print(fileName + "\n")
    print(os.path.abspath(os.path.join(folder_path , fileName))+ '\n')
    if(fileName.endswith('.png') or fileName.endswith('.jpg') ):
        print("3")    
        #Fimg = Image.open(fileName)
        #print(Fimg)
        print("4")
print("5")