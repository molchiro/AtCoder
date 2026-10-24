N, K = list(map(int, input().split()))

# dp[i][j][f]: i番目までみて、j回操作してて、連続裏返し操作中？

dp = [[-10**18]*2 for _ in range(12)]
dp[0][0] = 0

for _ in range(N):
    A, B = list(map(int, input().split()))
    ndp = [[-10**18]*2 for _ in range(12)]

    for j in range(K+1):
        # f=0 -> f=0
        ndp[j][0] = max(ndp[j][0], dp[j][0] + A)
        # f=0 -> f=1
        ndp[j+1][1] = max(ndp[j+1][1], dp[j][0] + B)
        # f=1 -> f=0
        ndp[j][0] = max(ndp[j][0], dp[j][1] + A)
        # f=1 -> f=1
        ndp[j][1] = max(ndp[j][1], dp[j][1] + B)

        
    dp = ndp


ans = -10**18
for j in range(K+1):
    for f in range(2):
        ans = max(ans, dp[j][f])
print(ans)