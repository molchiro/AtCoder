N = int(input())
P = list(map(float, input().split()))
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        p = P[i]
        dp[i+1][j] += dp[i][j]*(1-p)
        dp[i+1][j+1] += dp[i][j]*p
print(sum(dp[-1][N//2+1:]))