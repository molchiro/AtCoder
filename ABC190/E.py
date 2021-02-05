from collections import deque

N, M = list(map(int, input().split()))
g = [[] for _ in range(N)]
for _ in range(M):
    A, B = list(map(lambda x: int(x) - 1, input().split()))
    g[A].append(B)
    g[B].append(A)

K = int(input())
C = list(map(lambda x: int(x) - 1, input().split()))

prime_dist = [[float('inf')]*K for _ in range(K)]

for i, c in enumerate(C):
    dq = deque()
    dq.append(c)
    dist = [float('inf')]*N
    dist[c] = 0
    while dq:
        x = dq.popleft()
        d = dist[x]
        for y in g[x]:
            if dist[y] == float('inf'):
                dist[y] = d+1
                dq.append(y)

    prime_dist[i] = [dist[c] for c in C]

dp = [[float('inf')]*K for _ in range(1 << K)]
for i in range(K):
    dp[1 << i][i] = 1

for S in range(1 << K):
    for i in range(K):
        if S >> i & 1:
            continue
        for j in range(K):
            if not S >> j & 1:
                continue
            dp[S | 1 <<i][i] = min(dp[S | 1 <<i][i], dp[S][j] + prime_dist[j][i])

ans = min(dp[-1])
print(ans if ans != float('inf') else -1)