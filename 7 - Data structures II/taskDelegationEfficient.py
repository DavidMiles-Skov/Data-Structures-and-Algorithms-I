import heapq as hq
q = []

num = int(input())
for i in range(num):
    put = str(input())
    if len(put)>1:
        put = put.split()
        if put[0] == "N":
            a = -(int(put[-1]))
            b = int(put[1])
            toopl = (a, b)
            hq.heappush(q, toopl)
    else:
        u = hq.heappop(q)
        print(u[-1])
