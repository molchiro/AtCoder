

mod = 998244353
denominator = pow(N, mod - 2, mod)

N = int(input())
A = list(map(int, input().split()))
A.sort()

dp = [0]*(N+1)
for i in range(N):
    dp[i+1] = A[i] * denominator % mod

for i in range(N):
    dp_prev = dp[:]
    dp = [0]*N+1
    dp[0] += dp_prev[0]
    



# for t in range(X+1):
#     for d in T:
#         dp[t+d] += dp[t] * denominator % mod
#         dp[t+d] %= mod
