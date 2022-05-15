from collections import deque

N, M = map(int, input().split())

dependencies = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

adjList = [[] for _ in range(N)]
inDegrees = [0 for _ in range(N)]
for x, y in dependencies:
    adjList[y].append(x)
    inDegrees[x] += 1

id0 = deque(i for i, x in enumerate(inDegrees) if x == 0)

semesters = 0
while id0:
    semesters += 1
    for _ in range(len(id0)):
        course = id0.popleft()
        for depended in adjList[course]:
            inDegrees[depended] -= 1
            if inDegrees[depended] == 0:
                id0.append(depended)
    
print(semesters)