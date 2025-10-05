from collections import deque
INF = 10**18

T = int(input())
for _ in range(T):
    N, K = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = list(map(lambda x: int(x) - 1, input().split()))
        G[a].append(b)
        G[b].append(a)
    
    dist = [[dict() for _ in range(K)] for _ in range(N)]

    dq = deque()
    dist[0][0][-1] = 0
    dq.append((0, 0, -1))
    while dq:
        u, q, prev = dq.popleft()
        d = dist[u][q][prev]
        nq = (q+1)%K
        for v in G[u]:
            if v == prev:
                continue
            if u in dist[v][nq]:
                continue
            dist[v][nq][u] = d+1
            dq.append((v, nq, u))
    
    ans = []
    for i in range(1, N):
        if not dist[i][0]:
            ans.append(-1)
        else:
            x = min(dist[i][0].values())
            ans.append(x//K)
    print(*ans)