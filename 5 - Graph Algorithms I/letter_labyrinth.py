from collections import deque

def distanceToEnd(matrix):
    startr = 0
    startc = 0
    endr = len(matrix) - 1
    endc = len(matrix[0]) - 1
    # print(endr)
    # print(endc)
    
    discoveries = []
    distances = []
    # preds = []
    for _ in range(endr + 1):
        discoveries.append([0] * (endc + 1))
        distances.append([-1] * (endc + 1))
        # preds.append(["n"] * (endc + 1))
    
    discoveries[startr][startc] = 1
    distances[startr][startc] = 0
    q = deque()
    q.append((startr, startc))
    while q:
        r, c = q.popleft()
        letter = matrix[r][c]
        # print(r)
        # print(c)
        # print(len(discoveries), len(matrix))
        # print(len(discoveries[0]), len(matrix[0]))
        
        if r+1 <= endr and discoveries[r+1][c] == 0 and matrix[r+1][c] != letter:
            if r+1 == endr and c == endc:
                # preds[r+1][c] = "u"
                # for l in preds: print(l)
                # for l in distances: print(l)
                return distances[r][c] + 2
            discoveries[r+1][c] = 1
            distances[r+1][c] = distances[r][c] + 1
            # preds[r+1][c] = "u"
            q.append((r+1, c))
        if c+1 <= endc and discoveries[r][c+1] == 0 and matrix[r][c+1] != letter:
            if r == endr and c+1 == endc:
                # preds[r][c+1] = "l"
                # for l in preds: print(l)
                # for l in distances: print(l)
                return distances[r][c] + 2
            discoveries[r][c+1] = 1
            distances[r][c+1] = distances[r][c] + 1
            # preds[r][c+1] = "l"
            q.append((r, c+1))
        if r-1 >= 0 and discoveries[r-1][c] == 0 and matrix[r-1][c] != letter:
            discoveries[r-1][c] = 1
            distances[r-1][c] = distances[r][c] + 1
            # preds[r-1][c] = "d"
            q.append((r-1, c))
        if c-1 >= 0 and discoveries[r][c-1] == 0 and matrix[r][c-1] != letter:
            discoveries[r][c-1] = 1
            distances[r][c-1] = distances[r][c] + 1
            # preds[r][c-1] = "r"
            q.append((r, c-1))

N = int(input())
matrix = []
for _ in range(N):
    nl = []
    ln = input()
    for c in ln:
        nl.append(c)
    matrix.append(nl)

print(distanceToEnd(matrix))