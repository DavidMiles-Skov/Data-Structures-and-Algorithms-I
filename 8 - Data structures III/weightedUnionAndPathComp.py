def init(n):
    for i in range(n + 1):
        parents[i] = i 
        subGraphSize[i] = 1

def find(i):
    while parents[i] != i:
        #parents[i] = parents[parents[i]]
        i = parents[i]
    return i

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
            
listRange = int(input())
op = []
uno = []
dos = []
operationNumber = int(input())
        
parents = [0] * (listRange+1)
subGraphSize = [0] * (1+listRange)

init(listRange)

for i in range(operationNumber):
    put = str(input())
    put = put.split()
    if put[0] == "F":
        print(find(int(put[1])))
    else:
        weightedUnion(int(put[1]), int(put[-1]))