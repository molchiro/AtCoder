N, M = list(map(int, input().split()))
# 逆順のダイクストラみたいなことをする
G = [[] for _ in range(M)]
for _ in range(M):
    l, d, k, c, a, b = list(map(int, input().split()))
    G[b-1].append((a, l, d, k, c))

ans = [-1]*N

from heapq import heapify, heappop, heappush
hq = [(-float('inf'), N-1)]

while hq:
    t, u = heappop(hq)
    ans[u] = -t
    for v, l, d, k, c in G[u]:
        lim = - t - c
        if lim - l < 0:
            continue
        x = (lim - l)//d
        heappush((-l-d*min(x, k), v))
