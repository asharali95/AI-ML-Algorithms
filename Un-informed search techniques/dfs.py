dictree={'A':['B','C','D'],'B':['A','F'],'C':['A'],'D':['A','F'],'E':['B','F'],'F':['D','F']}
roottree=list(dictree.keys())
openlist=[]
closelist=[]
traversalturn=1
print("Graph:\n",dictree)
openlist.append(input("Select initial State: "))
goalstate = input("Select Final State:")
print(f"openlist:{openlist}\t\t\t\t\t closelist:{closelist}")
for vertextree in roottree:
    closelist.append(openlist.pop(0))
    if(closelist[-1]!= goalstate):
        i=dictree[vertextree]
        for neighbour in i[::-1]:
            if (neighbour not in openlist):
                openlist.insert(0,neighbour)
            print(f"openlist:{openlist}\t\t\t\t\t closelist:{closelist}")
    else:
        print(f"openlist:{openlist}\t\t\t\t\t closelist:{closelist}")
        break       
print("\n\n path:",end="-")
for i in closelist:
     print(i,end="-") 
                    
                    
          

                