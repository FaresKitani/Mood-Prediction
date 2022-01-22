import openpyxl
import pandas as pd

#df = pd.read_excel(r'C:\FARES-Lenove\Cooding\Main project\My_Excel.xlsx')


writer = pd.ExcelWriter('My_Excel1.xlsx' )



LE = pd.DataFrame({'left_eye': [41, 42, 43, 44]})
RE = pd.DataFrame({'right_eye': [41, 42, 43, 44]})
NS = pd.DataFrame({'nose': [41, 42, 43, 44]})
ML = pd.DataFrame({'mouth_left': [41, 42, 43, 44]})
MR = pd.DataFrame({'mouth_right': [41, 42, 43, 44]})


LE.to_excel(writer, sheet_name ='Sheet1',
             startrow = 0, startcol = 0,
             header = True, index = True)

RE.to_excel(writer, sheet_name ='Sheet1',
             startrow = 0, startcol = 2,
             header = True, index = False)

NS.to_excel(writer, sheet_name ='Sheet1',
             startrow = 0, startcol = 3,
             header = True, index = False)
MR.to_excel(writer, sheet_name ='Sheet1',
             startrow = 0, startcol = 4,
             header = True, index = False)

ML.to_excel(writer, sheet_name ='Sheet1',
             startrow = 0, startcol = 5,
             header = True, index = False)
print("done")

writer.save()

print ("df")
