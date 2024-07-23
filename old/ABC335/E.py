# 同じ数字を結ぶパスは同じものとみなす　=> UF
# 有向グラフとして扱う

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
paths = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

from atcoder.dsu import DSU

dsu = DSU(N)

for u, v in paths:
    if A[u] == A[v]:
        dsu.merge(u, v)

G = [[] for _ in range(N)]
for u, v in paths:
    ul = dsu.leader(u)
    vl = dsu.leader(v)
    if ul == vl:
        continue
    # print(ul, vl)
    if A[ul] < A[vl]:
        G[ul].append(vl)
    else:
        G[vl].append(ul)

from heapq import heapify, heappop, heappush

score = [0]*N
sl = dsu.leader(0)
gl = dsu.leader(N-1)
score[sl] = 1
hq = [(A[sl], sl)]
seen = [0]*N
while hq:
    a, u = heappop(hq)
    if seen[u]:
        continue
    seen[u] = 1
    for v in G[u]:
        score[v] = max(score[v], score[u]+1)
        heappush(hq, (A[v], v))
    
    # print(score)
print(score[gl])


