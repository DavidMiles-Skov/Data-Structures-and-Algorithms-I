adj_lst = []
s=input()
N, M = int(s.split()[0]), int(s.split()[1])

# Creating adjacency list
graph = {}

for i in range(1,N+1):
    graph[i]=[]
for i in range(1, M+1):
    s=input()
    x, y = int(s.split()[0]), int(s.split()[1])
    graph[x].append(y)

visited = set() # Set to keep track of visited nodes of graph.


def dfs(visited, graph, v, time):  #function for dfs 
    print(v)
    visited.add(v)
    for u in graph[v]:
        if u not in visited:
            dfs(visited,graph,u,time+1)
    print(time)

# Driver Code

dfs(visited,graph, N,0)
