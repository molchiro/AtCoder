N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, b = list(map(int, input().split()))
    G[u-1].append((b, v-1))
    G[v-1].append((b, u-1))

for i in range(N):
    G[i].sort()

ans = [-1]*N

from heapq import heapify, heappop, heappush

hq = []
hq.append((0, 0)) # (w, u)
while hq:
    w, u = heappop(hq)
    if ans[u] != -1:
        continue
    w += A[u]
    ans[u] = w
    for b, v in G[u]:
        heappush(hq, (w+b, v))

print(*ans[1:])

