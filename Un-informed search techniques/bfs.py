dictree={'A':['B','C','D'],'B':['A','F'],'C':['A'],'D':['A','F'],'E':['B','F'],'F':['D','F']}
roottree=list(dictree.keys())
openlist=[]
closelist=[]
traversalturn=1
print("Graph:\n",dictree)
openlist.append(input("Select initial State: "))
goalstate = input("Select Final State:")
print(f"\n-----{str(traversalturn)}----\n")
print(f"openlist:{openlist}\t\t\t\t closelist:{closelist}")

for vertextree in roottree:
    closelist.append(openlist.pop(0))
    traversalturn+=1
    print(f"\n-----{str(traversalturn)}----\n")
    if(closelist[-1]!= goalstate):
        i=dictree[closelist[-1]]
        for neighbour in i:
            if (neighbour not in openlist):
                openlist.append(neighbour)
        print(f"openlist:{openlist}\t\tcloselist:{closelist}")
    else:
        print(f"openlist:{openlist}\t\tcloselist:{closelist}")
        break;
print("\n\n path:",end="-")
for i in closelist:
    print(i,end="-")
    
    
    
    


    


