N, M = list(map(int, input().split()))
W = list(map(int, input().split()))
cost_min = [10**18]*N
cost_min[0] = 0
cost_max = [0]*N
cost_max[0] = 0
weight_max = [0]*N
weight_max[0] = W[0]

G = [[] for _ in range(N)]
for _ in range(M):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append(b)
    G[b].append(a)

from heapq import heapify, heappop, heappush

seen = [0]*N
# seen[0] = 1
hq = []
heappush(hq, (W[0], (0, 0))) # (w, (c, u))

while hq:
    w, (c, u) = heappop(hq)
    if seen[u] == 0:
        seen[u] = 1
        cost_min[u] = c
        cost_max[u] = c
        weight_max[u] = w
    else:
        # costもweightも最大を超えるなら来た意味は無い
        if c >= cost_max[u] and w >= weight_max[u]:
            continue
        cost_min[u] = min(cost_min[u], c)
        cost_max[u] = max(cost_max[u], c)
        weight_max[u] = max(weight_max[u], w)


    for v in G[u]:
        nc = c+w
        nw = w+W[v]
        heappush(hq, (nw, (nc, v)))


print(*cost_min, sep='\n')
