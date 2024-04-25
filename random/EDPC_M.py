# dp[i][j] i番目まで見て合計j個配るやりかた
# いもす法で区間更新する
mod = 10**9+7
N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

dp = [0]*(K+2)
dp[0] = 1
for a in A:
    ndp = [0]*(K+2)
    for i in range(K+1):
        ndp[i] += dp[i]
        ndp[i] %= mod
        ndp[min(K+1, i+a+1)] -= dp[i]
        ndp[min(K+1, i+a+1)] %= mod
    
    for i in range(K+1):
        ndp[i+1] += ndp[i]
        ndp[i+1] %= mod
    
    dp = ndp
    # print(dp)

print(dp[K])
