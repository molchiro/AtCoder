N = int(input())
G = [[] for _ in range(N)]
for i in range(N-1):
    A, B, X = list(map(int, input().split()))
    G[i].append((i+1, A))
    G[i].append((X-1, B))

from heapq import heapify, heappop, heappush

hq = [(0, 0)]
seen = [0]*N
while hq:
    D, u = heappop(hq)
    if seen[u]:
        continue
    seen[u] = 1
    # print(D, u)
    if u == N-1:
        print(D)
        break
    for v, d in G[u]:
        heappush(hq, (D+d, v))