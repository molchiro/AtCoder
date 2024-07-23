H, W = list(map(int, input().split()))
field = [[-1]*(W+2)] + [[-1]+ [0]*W + [-1] for _ in range(H)] + [[-1]*(W+2)]
for h in range(H):
    A = input()
    for w in range(W):
        x = A[w]
        if x == '#':
            field[h+1][w+1] = -1
        elif x == 'S':
            S = (h+1, w+1)        
        elif x == 'T':
            T = (h+1, w+1)
nodes = dict()
nodes[S] = []
nodes_set = set()
nodes_set.add(S)
nodes_set.add(T)
# print(nodes_set)
N = int(input())
from collections import deque
medicines = []
for _ in range(N):
    R, C, E = list(map(int, input().split()))
    medicines.append((R, C, E))
    nodes_set.add((R, C))
    nodes[(R, C)] = []
# print(medicines)
for R, C, E in medicines:
    # print('med', R, C, E)
    seen = [[1]*(W+2)] + [[1]+ [0]*W + [1] for _ in range(H)] + [[1]*(W+2)]
    dq = deque()
    dq.append((R, C, E))
    while dq:
        r, c, e = dq.popleft()
        # print(r, c, e)
        if seen[r][c]:
            continue
        seen[r][c] = 1
        if (r, c) in nodes_set:
            nodes[(R, C)].append((r, c))
        
        if e <= 0:
            continue

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if field[r+dr][c+dc] == 0:
                dq.append((r+dr, c+dc, e-1))

# print(nodes)

seen = [[1]*(W+2)] + [[1]+ [0]*W + [1] for _ in range(H)] + [[1]*(W+2)]
dq = deque()
dq.append(S)
while dq:
    node = dq.popleft()
    r, c = node
    if seen[r][c]:
        continue
    seen[r][c] = 1
    if node == T:
        print('Yes')
        exit()

    for to in nodes[node]:
        dq.append(to)

print('No')