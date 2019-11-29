import re

#Lists of each skill, each list has all the queue data
#0- Skill Name
#1- Agents Staffed
#2- Agents Avail
#3- Agents on ACD Calls
#4- Agents in ACW
#5- Agents in Other
#6- Agents in Aux        Minus those on Dialer
#7- Dialer
#8- Calls Waiting
#9- Oldest Call Waiting
#10- ACD Calls
#11- Avg ACD Time
#12- Aban Calls
#13- % Aban Calls
#14- Avg Aban Time
#15- Avg Speed Ans
#16- Service Level

def get_skills():
    delimiters = '\t', '\n'
    regexPattern = '|'.join(map(re.escape, delimiters))

    qc1 = open('R:\\Operations\\Ben\\Macro\\SCE\\qc1.txt')
    qc1 = qc1.read()
    qc1 = re.split(regexPattern, qc1)

    Skills = []
    k = 0
    for i in range(len(qc1)):
        
        if qc1[i].startswith('SCE'):
            
            Skills.append([])
            j = 0
            while j <= 16:
                
                Skills[k].append(qc1[i+j])
                j += 1
            k += 1
    return Skills

def get_totals():
    delimiters = '\t', '\n'
    regexPattern = '|'.join(map(re.escape, delimiters))

    qc1 = open('R:\\Operations\\Ben\\Macro\\SCE\\qc1.txt')
    qc1 = qc1.read()
    qc1 = re.split(regexPattern, qc1)

    Skills = []
    k = 0
    for i in range(len(qc1)):
        
        if qc1[i].startswith('SCE'):
            
            Skills.append([])
            j = 0
            while j <= 16:
                
                Skills[k].append(qc1[i+j])
                j += 1
            k += 1

    listStaffed = []
    Staffed = 0
    listAvail = []
    Avail = 0
    ACD = 0
    ACW = 0
    Other = 0
    Aux = 0
    Dialer = 0
    CallsWaiting = 0
    Oldest = 0
    ACDCalls = 0
    AvgACD = 0
    Aban = 0
    AbanPer = 0
    AvgAban = 0
    ASA = 0
    SL = 0

    #Calculates the totals
    Totals = []
    Totals.append('Totals')
    for i in range(len(Skills)):
        listStaffed.append(int(Skills[i][1]))
        listAvail.append(int(Skills[i][2]))
        ACD += int(Skills[i][3])
        ACW += int(Skills[i][4])
        Other += int(Skills[i][5])
        Aux += int(Skills[i][6])
        Dialer += int(Skills[i][7])
        CallsWaiting += int(Skills[i][8])
        Oldest += (float(Skills[i][9]) * float(Skills[i][8]))
        ACDCalls += int(Skills[i][10])
        AvgACD += (float(Skills[i][11]) * float(Skills[i][10]))
        Aban += int(Skills[i][12])
        AbanPer += (int(Skills[i][13]) * int(Skills[i][12]))
        AvgAban += (float(Skills[i][14]) * float(Skills[i][12]))
        ASA += (float(Skills[i][15]) * float(Skills[i][10]))
        SL += (float(Skills[i][16]) * float(Skills[i][10]))


    Staffed = max(listStaffed)
    Avail = max(listAvail)
    
    #catches 0s before trying to calculate
    if CallsWaiting == 0:
        Oldest = 0
    else:
        Oldest = Oldest / CallsWaiting

    if ACDCalls == 0:
        AvgACD = 0
        ASA = 0
        SL = 0
    else:
        AvgACD = AvgACD / ACDCalls
        ASA = ASA / ACDCalls
        SL = SL / ACDCalls

    if Aban == 0:
        AbanPer = 0
        AvgAban = 0
    else:
        AbanPer = AbanPer / Aban
        AvgAban = AvgAban / Aban

    Totals.extend((Staffed, Avail, ACD, ACW, Other, Aux, Dialer, CallsWaiting, Oldest, ACDCalls, AvgACD, Aban, AbanPer, AvgAban, ASA, SL))
    return Totals
