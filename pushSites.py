import os
import time
import bs4
from bs4 import BeautifulSoup

TimeOf = "Last Update: %s" % time.ctime(os.path.getmtime('R:\\Operations\\Ben\\Macro\\SCE\\qc1.txt'))

def update_East(CallsWaiting, ServiceLevel, Available):
    soup = BeautifulSoup(open('R:\\Operations\\Ben\\Macro\\HTML\\DashBoard\\Sites\\SCE_East_DB.html'))
    ID_CALL_VOL = soup.find_all(id='Call_Vol')
    ID_SERV_LVL = soup.find_all(id='Serv_Lev')
    ID_AVAIL_AG = soup.find_all(id='Avail_Ag')
    ID_TIME_UP = soup.find_all(id='TimeUp')
    ID_CALL_VOL[0].string = str(CallsWaiting)
    ID_SERV_LVL[0].string = str('{:04.2f}'.format(ServiceLevel) + '%')
    ID_AVAIL_AG[0].string = str(Available)
    ID_TIME_UP[0].string = str(TimeOf)
    with open('R:\\Operations\\Ben\\Macro\\HTML\\DashBoard\\Sites\\SCE_East_DB.html', 'w') as fp2:
        fp2.write(str(soup))

def update_Cove(CallsWaiting, ServiceLevel, Available):
    soup = BeautifulSoup(open('R:\\Operations\\Ben\\Macro\\HTML\\DashBoard\\Sites\\SCE_Cove_DB.html'))
    ID_CALL_VOL = soup.find_all(id='Call_Vol')
    ID_SERV_LVL = soup.find_all(id='Serv_Lev')
    ID_AVAIL_AG = soup.find_all(id='Avail_Ag')
    ID_TIME_UP = soup.find_all(id='TimeUp')
    ID_CALL_VOL[0].string = str(CallsWaiting)
    ID_SERV_LVL[0].string = str('{:04.2f}'.format(ServiceLevel) + '%')
    ID_AVAIL_AG[0].string = str(Available)
    ID_TIME_UP[0].string = str(TimeOf)
    with open('R:\\Operations\\Ben\\Macro\\HTML\\DashBoard\\Sites\\SCE_Cove_DB.html', 'w') as fp2:
        fp2.write(str(soup))

def update_West(CallsWaiting, ServiceLevel, Available):
    soup = BeautifulSoup(open('R:\\Operations\\Ben\\Macro\\HTML\\DashBoard\\Sites\\SCE_West_DB.html'))
    ID_CALL_VOL = soup.find_all(id='Call_Vol')
    ID_SERV_LVL = soup.find_all(id='Serv_Lev')
    ID_AVAIL_AG = soup.find_all(id='Avail_Ag')
    ID_TIME_UP = soup.find_all(id='TimeUp')
    ID_CALL_VOL[0].string = str(CallsWaiting)
    ID_SERV_LVL[0].string = str('{:04.2f}'.format(ServiceLevel) + '%')
    ID_AVAIL_AG[0].string = str(Available)
    ID_TIME_UP[0].string = str(TimeOf)
    with open('R:\\Operations\\Ben\\Macro\\HTML\\DashBoard\\Sites\\SCE_West_DB.html', 'w') as fp2:
        fp2.write(str(soup))
