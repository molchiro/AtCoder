from atcoder.math import inv_mod

MOD = 998244353
INV_MOD_2 = inv_mod(2, MOD)

N = int(input())
table_2 = [1]
tmp = 1
for _ in range(3001):
    tmp *= 2
    tmp %= MOD
    table_2.append(tmp)
cumsum_2 = [0]
for i in range(3001):
    cumsum_2.append((cumsum_2[-1]+table_2[i])%MOD)
# print(table_2)
# print(cumsum_2[:5])
dp = [[0]*(N) for _ in range(N)]
dp[0][0] = 1
for r in range(1, N):
    # dp[0][r]を求める
    x = table_2[r]
    # print(x)
    for l in range(r):
        x -= dp[l][r-1-l] * (cumsum_2[r]-cumsum_2[l])%MOD
        x %= MOD
    # print(x)
    x *= inv_mod(cumsum_2[r+1], MOD)
    x %= MOD
    dp[0][r] = x
    # dp[l][r-l] (l: 1->r) を求める 
    for l in range(1, r+1):
        dp[l][r-l] = ((dp[l-1][r-l]+dp[l-1][r-l+1])*INV_MOD_2)%MOD

# print(dp)
for l in range(N):
    print(dp[l][N-l-1])