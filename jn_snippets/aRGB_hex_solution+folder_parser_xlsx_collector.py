path_dir = Path("../data/")


#color aRGB must be hex SOLUTION

import win32com.client as win32
import openpyxl
import pandas


def openWorkbook(xlapp, xlfile):
    try:        
        xlwb = xlapp.Workbooks(xlfile)            
    except Exception as e:
        try:
            xlwb = xlapp.Workbooks.Open(xlfile)
        except Exception as e:
            print(e)
            xlwb = None                    
    return(xlwb)


def read_excel_2(filepath):
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = openWorkbook(excel, filepath)
    ws = wb.ActiveSheet
    df = pandas.DataFrame(ws.UsedRange())
    wb.Close()
    return df




#xlsx parser & collector

import os
import pandas as pd

path_dir = Path("../data/")
listof_files = os.listdir(path_dir)
current_file_name = os.path.dirname(os.path.abspath("__file__"))

#flag to make sure append is happening properly
count = 0
mainFrame = 0

for file in listof_files:
    #To ignore the python script file for pd.read_excel
    if((file != current_file_name) and (file.endswith(".xlsx"))):
        print(file)
        tempdf = read_excel_2(r"C:\Users\fomkin.ag\Documents\dzm_hospital\data\\" + str(file))
        tempdf = tempdf[3:-1]
        

        if(count == 0): 
            mainFrame = tempdf.copy()
        else: 
            mainFrame = pd.concat([mainFrame,tempdf])

        count += 1

mainFrame.to_excel('final.xlsx',index=False)  