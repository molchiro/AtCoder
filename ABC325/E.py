N, A, B, C = list(map(int, input().split()))
G = [[] for _ in range(N*2)]
for i in range(N):
    D = list(map(int, input().split()))
    for j, d in enumerate(D):
        # 車移動
        G[i].append((j, d*A))
        # 電車移動
        G[i+N].append((j+N, d*B+C))
    # 電車のりかえ
    G[i].append((i+N, 0))

ans = [float('inf')]*(N*2)
from heapq import heapify, heappop, heappush
hq = [(0, 0)]
heapify(hq)
while hq:
    d, u = heappop(hq)
    if ans[u] != float('inf'):
        continue
    ans[u] = d

    if u == N-1 or u == 2*N-1:
        print(ans[u])
        exit()

    for to, cost in G[u]:
        heappush(hq, (d+cost, to))
