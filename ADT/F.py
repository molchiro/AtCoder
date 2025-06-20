N, M, K = list(map(int, input().split()))
K -= N
MOD = 998244353

# dp[i][j]: i桁目まで見て 今までの合計がjである

dp = [0]*(K+1)
dp[0] = 1
for _ in range(N):
    ndp = [0]*(K+1)
    for k in range(K+1):
        for n in range(M):
            if k+n <= K:
                ndp[k+n] += dp[k]
    
    for k in range(K+1):
        ndp[k] %= MOD

    dp = ndp
    # print(dp)

print(sum(dp)%MOD)
