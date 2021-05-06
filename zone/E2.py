from heapq import heapify, heappop, heappush

R, C = list(map(int, input().split()))
# 頂点倍加し、落下中を表現する
G = [[] for _ in range(2*C*R)]
# 通常の移動
for r in range(R):
    A = list(map(int, input().split()))
    for c in range(C-1):
        G[r*C+c].append((A[c], r*C+c+1))
        G[r*C+c+1].append((A[c], r*C+c))
for r in range(R-1):
    B = list(map(int, input().split()))
    for c in range(C):
        G[r*C+c].append((B[c], (r+1)*C+c))
# 落下
for r in range(R):
    for c in range(C):
        G[r*C+c].append((1, r*C+c+C*R))
        G[r*C+c+C*R].append((0, r*C+c))
for r in range(R-1):
    for c in range(C):
        G[(r+1)*C+c+C*R].append((1, r*C+c+C*R))
# dijkstra
dist = [10**6]*(2*C*R)
hq = [(0, 0)]
while hq:
    d, v = heappop(hq)
    if d > dist[v]:
        continue
    dist[v] = d
    if v == R*C-1:
        print(dist[v])
        exit()
    for dd, to in G[v]:
        if d+dd < dist[to]:
            dist[to] = d+dd
            heappush(hq, (d+dd, to))