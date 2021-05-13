INF_V = 1000*100
N, W = list(map(int, input().split()))
dp = [[W+1]*(INF_V+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    w, v = list(map(int, input().split()))
    for j in range(INF_V-1000+1):
        dp[i+1][j+v] = min(dp[i+1][j+v], dp[i][j] + w)
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
print([i for (i, w) in enumerate(dp[N]) if w <= W][-1])