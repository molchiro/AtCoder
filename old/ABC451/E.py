N = int(input())
d = [list(map(int, input().split())) for _ in range(N-1)]

print(d)

edges = [[] for _ in range(10000)]

for i in range(N-1):
    for j in range(N-1-i):
        A = d[i][j]
        edges[A].append((i, i+j+1))

print(edges)

from atcoder.dsu import DSU

dsu = DSU(N)

# 重みが小さい辺から貪欲に繋いで成功するか確認する

rem = N-1
for i in range(10000):
    candidates = edges[i]
    if len(candidates) == 0:
        continue

    if len(candidates) > rem:
        break
    
    for u, v in candidates:
        if dsu.same(u, v):
            