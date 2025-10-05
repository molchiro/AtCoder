from heapq import heapify, heappop, heappush
INF = 10**18

T = int(input())
for _ in range(T):
    N, K = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = list(map(lambda x: int(x) - 1, input().split()))
        G[a].append(b)
        G[b].append(a)
    
    dist = [[INF]*K for _ in range(N)]

    hq = []
    heappush(hq, (0, 0, 0))
    while hq:
        d, u, q = heappop(hq)
        if dist[u][q] < d:
            continue

        nq = (q+1)%K
        for v in G[u]:
            if d+1 > dist[v][nq]:
                continue
            dist[v][nq] = d+1
            heappush(hq, (d+1, v, nq))
    
    ans = []
    for i in range(1, N):
        if dist[i][0] == INF:
            ans.append(-1)
        else:
            ans.append(dist[i][0]//K)
    print(*ans)