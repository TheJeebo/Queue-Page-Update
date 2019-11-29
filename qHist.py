import os
import time
from datetime import datetime

TimeOf2 = datetime.strptime(time.ctime(os.path.getmtime('R:\\Operations\\Ben\\Macro\\SCE\\qc1.txt')), "%a %b %d %H:%M:%S %Y")

def fullPath():
    Mon1 = datetime.now().strftime('%m')
    Day1 = datetime.now().strftime('%d')
    fName =  Mon1 + '_' + Day1 + '_qt.txt'
    fName_SL =  Mon1 + '_' + Day1 + '_SL_qt.txt'
    fPath = 'R:\\Operations\\Ben\\Macro\\SCE\\Q_Hist\\'
    newPath = fPath + fName_SL
    return newPath

def save_hist_w_SL(CallsWaiting, ServiceLevel):
    fi = open(fullPath(), 'a')
    fi.write("\n" + str(TimeOf2) + ", " + str(CallsWaiting) + ", " + str(ServiceLevel))
    fi.close()
