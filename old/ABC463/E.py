N, M, Y = list(map(int, input().split()))
G = [[] for _ in range(N+2)]
for _ in range(M):
    a, b, T = list(map(lambda x: int(x) - 1, input().split()))
    T += 1
    G[a].append((b, T))
    G[b].append((a, T))

X = list(map(int, input().split()))
for i in range(N):
    # 超頂点1への辺と超頂点2から出る辺を張る
    G[i].append((N, X[i]))
    G[N+1].append((i, X[i]))
# 超頂点1から超頂点2への辺
G[N].append((N+1, Y))


ans = [10**18]*(N+2)
from heapq import heapify, heappop, heappush

hq = [(0, 0)]
while hq:
    d, u = heappop(hq)
    if ans[u] < d:
        continue

    for v, cost in G[u]:
        if d+cost < ans[v] :
            ans[v] = d+cost
            heappush(hq, (d+cost, v))

print(*ans[1:N])