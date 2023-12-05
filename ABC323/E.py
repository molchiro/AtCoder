# dp[t] t秒後にちょうど曲が終わっている確率


N, X = list(map(int, input().split()))
T = list(map(int, input().split()))

mod = 998244353
denominator = pow(N, mod - 2, mod)
# print(c * denominator % mod)

dp = [0]*100000
dp[0] = 1
for t in range(X+1):
    for d in T:
        dp[t+d] += dp[t] * denominator % mod
        dp[t+d] %= mod

ans = 0
for t in range(X, max(-1, X-T[0]), -1):
    ans += dp[t] * denominator % mod
    ans %= mod

# dp = [0]*100000
# dp[0] = 1
# for t in range(X+1):
#     for d in T:
#         dp[t+d] += dp[t] / N

# print(dp[:10])

# ans = 0
# for t in range(X, max(-1, X-T[0]), -1):
#     ans += dp[t]/N

print(ans)