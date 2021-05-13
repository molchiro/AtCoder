from heapq import heappop, heappush

N, M, X, Y = list(map(int, input().split()))
X -= 1
Y -= 1

g = [[] for _ in range(N)]
for _ in range(M):
    A, B, T, K = list(map(int, input().split()))
    A -= 1
    B -= 1
    g[A].append((B, T, K))
    g[B].append((A, T, K))

dist = [float('inf')]*N
hq = [(0, X)]
while hq:
    d, v = heappop(hq)
    if dist[v] != float('inf'):
        continue
    dist[v] = d
    for to, t, k in g[v]:
        heappush(hq, (d + t + (k-d)%k, to))

ans = dist[Y]
print(ans if ans != float('inf') else -1)