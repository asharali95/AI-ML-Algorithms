noOfGenes = eval(input("Enter number of genes: "))
noOfChromosomes = eval(input("Enter no of chromosomes: "))
index = 0
S=[]
tempList = []

for gene in range(noOfGenes):
    print("Enter chromosomes of gene",index+1,"(must be 0 and 1 only): ")
    for chromosomes in range(noOfChromosomes):
        tempList.append(eval(input()))
    S.append(tempList)
    print(S)
    tempList=[]
    index=index+1

def calfitness(S):
    total=0
    print("Applying Fitness...")
    for i in S:
        total+=i.count(1)
    return total;
fit=calfitness(S)
print("Fitness Applied Successfully")

print("Arranging in Descending order")
desc=S
for i in range(len(desc)):
    j=i + 1
    for j in range(len(desc)):
        if desc[i].count(1)>desc[j].count(1):
           desc[j],desc[i]=desc[i],desc[j]
print("s =" , desc)
print("Cross over after 2 points")
for i in range(4):
    desc[1][i],desc[2][i]=desc[2][i],desc[1][i]
    desc[1],desc[2]=desc[2],desc[1]
print("s2 and s3")
print("s2=", desc[1], "s3=", desc[2])
print("s=", desc)
print("Mutation")
for i in range(6):
    for j in range(2):
        if(desc[i][j]==0):
            desc[i][j]=1
        else:
            desc[i][j]=0
print("s=",desc)
fit2=calfitness(desc)
if fit<fit2:
    print("Old Fitness is greater after applying Genetic Algorithm")
    print("old fitness: ",fit)
    print("updated fitness: ",fit2)
else:
    print("Old Fitness is greater before applying Genetic Algorithm")
    print("old fitness: ",fit)
    print("updated fitness: ",fit2)
