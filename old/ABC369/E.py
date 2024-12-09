INF = 10**18
N, M = list(map(int, input().split()))

bridges = []
for _ in range(M):
    u, v, t = list(map(int, input().split()))
    bridges.append((u-1, v-1, t))

G = [[INF]*N for _ in range(N)]
for i in range(N):
  G[i][i] = 0

for u, v, t in bridges:
    G[u][v] = min(G[u][v], t)
    G[v][u] = min(G[v][u], t)

dp = []
for i in range(N):
    dp.append(G[i][:])

# 3重ループで全ての頂点の間の距離を求める．
for k in range(N):
    for i in range(N):
        for j in range(N):
            if(dp[i][k] == INF or dp[k][j] == INF):
                continue
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
            
from itertools import permutations

Q = int(input())
for _ in range(Q):
    K = int(input())
    B = list(map(lambda x: int(x) - 1, input().split()))
    ans = INF
    for order in permutations(B, K):
        for mask in range(1<<K):
            tour = [0]
            d = 0
            for i in range(K):
                u, v, t = bridges[order[i]]
                if mask >> i & 1:
                    tour.append(v)
                    tour.append(u)
                else:
                    tour.append(u)
                    tour.append(v)
                d += t
            tour.append(N-1)
            # print(tour)
            for i in range(K+1):
                d += dp[tour[2*i]][tour[2*i+1]]
            ans = min(ans, d)
    print(ans)

            
