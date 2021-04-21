noOfChromosomes = eval(input("Enter number of chromosomes: "))
noOfGenes = eval(input("Enter no of genes: "))
index = 0
S=[]
tempList = []

for choromosome in range(noOfChromosomes):
    print("Enter genes of chromosome",index+1,"(must be 0 and 1 only): ")
    for gene in range(noOfGenes):
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
print("==Cross over==")
crossOver = eval(input("Crossover after which point? "))
for i in range(crossOver,noOfGenes):
    desc[1][i],desc[2][i]=desc[2][i],desc[1][i]
    desc[1],desc[2]=desc[2],desc[1]
print("s2 and s3")
print("s2=", desc[1], "s3=", desc[2])

print("==Mutation==")
for i in range(noOfChromosomes):
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

