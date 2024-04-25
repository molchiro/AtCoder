N, M = list(map(int, input().split()))
INF = float('inf')

dp = [[INF]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0
for _ in range(M):
    A, B, C = list(map(int, input().split()))
    dp[A-1][B-1] = C

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
            if dp[i][j] != INF:
                ans += dp[i][j]
print(ans)