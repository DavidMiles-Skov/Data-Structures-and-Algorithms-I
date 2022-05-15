put = str(input())  
put = put.split()

compNum = int(put[0])
opNum = int(put[-1])

def init(n):
    for i in range(n + 1):
        parents[i] = i 
        subGraphSize[i] = 1
  
#Find with path compression 
def find(i):
    while parents[i] != i:
        #parents[i] = parents[parents[i]]
        i = parents[i]
    return i
  
    

#Weighted Union
def weightedUnion(x,y):
    rI = find(x)
    rJ = find(y)
    if rI != rJ:
        if subGraphSize[rI] < subGraphSize[rJ]:
            parents[rI] = parents[rJ]
            subGraphSize[rJ] = subGraphSize[rJ] + subGraphSize[rI]
        else:
            parents[rJ] = parents[rI]
            subGraphSize[rI] = subGraphSize[rJ] + subGraphSize[rI]


length = compNum+1
parents = [0] * length
subGraphSize = [0] * length
init(compNum)



for i in range(opNum):
    putput = str(input())
    putput = putput.split()
    if putput[0] == "C":
        if find(int(putput[1])) == find(int(putput[-1])):
            print("YES")
        else:
            print("NO")
    else:
        weightedUnion(int(putput[1]), int(putput[-1]))