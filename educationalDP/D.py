N, W = list(map(int, input().split()))
dp = [[0]*(W+1) for _ in range(N+1)]
for i in range(N):
    w, v = list(map(int, input().split()))
    for j in range(W+1):
        if j + w <= W:
            dp[i+1][j+w] = max(dp[i+1][j+w], dp[i][j] + v)
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
print(max(dp[N]))