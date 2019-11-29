import sys
sys.path.insert(1, 'R:\\Operations\\Ben\\Macro\\HTML\\DashBoard\\Py\\QueueUpdate')
import graph_Q
import gatherQ
import qHist
import pushSites
import pushQ

#Gathers Queue info
Totals = gatherQ.get_totals()
Skills = gatherQ.get_skills()

#Save Queue History
qHist.save_hist_w_SL(Totals[8], Totals[16])

#Drop it in each site HTML
pushSites.update_East(Totals[8], Totals[16], Totals[2])
pushSites.update_Cove(Totals[8], Totals[16], Totals[2])
pushSites.update_West(Totals[8], Totals[16], Totals[2])

#Update the Queues page
pushQ.update_Queues(Totals, Skills)

#update graph
graph_Q.update_graph()
