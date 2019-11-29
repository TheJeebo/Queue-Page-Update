import re
from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def update_graph():
    Mon1 = datetime.now().strftime('%m')
    Day1 = datetime.now().strftime('%d')
    fName =  Mon1 + '_' + Day1 + '_SL_qt.txt'
    fPath = 'R:\\Operations\\Ben\\Macro\\SCE\\Q_Hist\\'

    Title = 'SCE - Queue & Service Level'
    xTitle = 'Time of Day'
    yTitle = 'Calls Waiting'
    y2Title = 'Service Level'

    delimiters = ',', '\n'
    regexPattern = '|'.join(map(re.escape, delimiters))

    qtF = open(fPath + fName)
    qtF = qtF.read()
    qtF = re.split(regexPattern, qtF)

    qtX = []
    qtY = []
    qtY2 = []

    j = 1
    for i in range(len(qtF)):
        if qtF[i] != '':
            if j == 1:
                qtX.append(qtF[i])
                j += 1
            elif j == 2:
                qtY.append(qtF[i])
                j += 1
            elif j == 3:
                qtY2.append(qtF[i])
                j = 1

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Scatter(x=qtX, y=qtY, name=yTitle),secondary_y=False,)
    fig.add_trace(go.Scatter(x=qtX, y=qtY2, name=y2Title),secondary_y=True,)

    fig.update_layout(xaxis=dict(title=xTitle))

    annotations = []
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05, xanchor='left',
                            yanchor='bottom', text=Title, font=dict(family='Arial',
                                                                    size=30, color='rgb(37,37,37)'),
                            showarrow=False))

    fig.update_layout(annotations=annotations)
    fig.update_layout(hovermode='x')

    fig.write_html('R:\\Operations\\Ben\\Macro\\HTML\\DashBoard\\Py\\SCE_Queue_Detail2.html', auto_open=False)
