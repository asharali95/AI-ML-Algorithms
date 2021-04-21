'''graph={'s':['a','b'],'a':['b','c','d'],'b':['c','d'],'c':['d'],'d':[] }
pathcost = {'sa':3,'sb':2,'ab':3,'ac':1,'ad':3,'bc':5,'bd':3,'cd':2}
hcost = {'s':1, 'a':3, 'b':3, 'c':0, 'd':0}
start=input("Enter start state:");
goal = input("Enter goal state: ");
ls = [start]
lscost = [hcost[start]]
print(lscost)
closelist=[]
print(ls,"\t\t\t\t closelist")
while len(ls)>0:
    min_index = lscost.index(min(lscost))
    cost = lscost.pop(min_index)
    n = ls.pop(min_index)
    cn = n[len(n)-1]
    if cn == goal:
        closelist.append(n)
        break
    nodes= graph[cn]
    nmin = pathcost[cn+nodes[0]]+cost
    for i in nodes:
        ls.append(n+i)
        lscost.append(cost+pathcost[cn+i]+hcost[i]-hcost[cn])
    closelist.append(n)
    print(ls,"\t\t\t",closelist)
print(ls,"\t\t\t",closelist)'''
#---------------------------------------------------------------
graph={'S':['A','B'],'A':['G'],'B':['G'],'G':[], }
pathcost = {'SA':2,'SB':2,'AG':2,'BG':2}
hcost = {'S':3, 'A':2, 'B':1, 'G':0}
start=input("Enter start state:");
goal = input("Enter goal state: ");
ls = [start]
lscost = [hcost[start]]
print(lscost)
closelist=[]

while len(ls)>0:
    min_index = lscost.index(min(lscost))
    cost = lscost.pop(min_index)
    n = ls.pop(min_index)
    cn = n[len(n)-1]
    if cn == goal:
        closelist.append(n)
        break
    nodes= graph[cn]
    nmin = pathcost[cn+nodes[0]]+cost
    for i in nodes:
        ls.append(n+i)
        lscost.append(cost+pathcost[cn+i]+hcost[i]-hcost[cn])
    closelist.append(n)
    print(ls,"\t\t\t",closelist)
print(ls,"\t\t\t",closelist)
