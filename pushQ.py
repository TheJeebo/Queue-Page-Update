import os
import time
import bs4
from bs4 import BeautifulSoup

def update_Queues(Totals, Skills):
    TimeOf = "Last Update: %s" % time.ctime(os.path.getmtime('R:\\Operations\\Ben\\Macro\\SCE\\qc1.txt'))

    #now for the big one
    soup = BeautifulSoup(open('R:\\Operations\\Ben\\Macro\\HTML\\DashBoard\\Queue_DB.html'))

    TempID = ''
    for i in range(18):
        for j in range(16):
            TempID = 'r' + str(i+1) + 'c' + str(j+1)
            TempSlot = soup.find_all(id=TempID)

   	    #fill in the table		
            if i == 17:
                if j == 8 or j == 10 or j == 12 or j == 13 or j == 14:
                    TempSlot[0].string = str('{:04.2f}'.format(float(Totals[j+1])))
                elif j == 15:
                    TempSlot[0].string = str('{:04.2f}'.format(float(Totals[j+1])) + '%')
                else:
                    TempSlot[0].string = str(Totals[j+1])
            else:
                if j == 10 or j == 13 or j == 14:
                    TempSlot[0].string = str('{:04.2f}'.format(float(Skills[i][j+1])))
                elif j == 15:
                    TempSlot[0].string = str('{:04.2f}'.format(float(Skills[i][j+1])) + '%')
                else:
                    TempSlot[0].string = str(Skills[i][j+1])
        
    ID_TIME_UP = soup.find_all(id='TimeUp')
    ID_TIME_UP[0].string = str(TimeOf)

    with open('R:\\Operations\\Ben\\Macro\\HTML\\DashBoard\\Queue_DB.html', 'w') as fp2:
        fp2.write(str(soup))
