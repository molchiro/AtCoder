N = int(input())
T = list(map(int, input().split()))

# dp[i][j] = i個目まで見て合計がjである組み合わせが存在するかどうか
dp = [[0]*(10**5+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(1000*i+1):
        if dp[i][j]:
            dp[i+1][j] = 1
            dp[i+1][j+T[i]] = 1

ans = float('inf')
total_T = sum(T)
for j in range(10**5+1):
    if dp[N][j]:
        ans = min(ans, max(total_T-j, j))
print(ans)