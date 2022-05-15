import heapq as hq
q = []

num = int(input())
for i in range(num):
    put = str(input())
    if len(put)>1:
        put = put.split()
        if put[0] == "I":
            hq.heappush(q, -(int(put[-1])))
    elif put == "P":
        for i in range(len(q)):
            print(-q[i], end = ' ')
    else:
        print(-1 * hq.heappop(q))
