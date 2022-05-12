
d = {}
N = int(input())
for i in range(N):
    x = int(input())
    if x in d:
        d[x]+=1
    else:
        d[x]=1
n_wrong = 0
for key,val in zip(d.keys(),d.values()):
    if val > 1:
        n_wrong+=1
print(n_wrong)