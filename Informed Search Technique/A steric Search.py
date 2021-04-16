dictree={'A':['B','E','C'],'B':['E','D'],'C':['F','G'],'D':[], 'E':[],'F':[],'G':[] }
roottree=list(dictree.keys())
openlist=['A']
closelist=[]
goalstate='G'
traversalturn=1
print(f"\n------{str(traversalturn)}-----\n")
print(f"openlist: {openlist} \t\t\t\t\t closelist:{closelist}")
for vertextree in roottree:
    closelist.append(openlist.pop(0))
    traversalturn+=1
    print(f"\n------{str(traversalturn)}-----")
    if (closelist[-1]!=goalstate):
	    i=dictree[closelist[-1]]
	    for neighbours in i:
		    if(neighbours not in openlist):
		        openlist.append(neighbours)
	    print(f"openlist: {openlist} \t\t\t\t\t closelist:{closelist}")
    else:
        print(f"openlist: {openlist} \t\t\t\t\t closelist:{closelist}")
        break
print("\n\n path:",end="-")
for i in closelist:
    print(i,end="-")