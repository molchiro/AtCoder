mod = 998244353

N, K = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(K)]
dp = [0]*(2*N+10)
dp[0] = 1
tmp = 0
for i in range(N):
    tmp += dp[i]
    tmp %= mod
    for L, R in S:
        dp[i+L] += tmp
        dp[i+R+1] -= tmp
print(dp[N-1]%mod)