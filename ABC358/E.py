mod = 998244353



N = 10 ** 4  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

K = int(input())
C = list(map(int, input().split()))
dp = [0]*(K+1)
dp[0] = 1
for c in C:
    # ndp = [0]*(K+1)
    # ndp[0] = 1
    ndp = dp[:]
    for i in range(K):
        for j in range(1, c+1):
            if i+j <= K:
                ndp[i+j] += (dp[i]*cmb(i+j, j, mod))%mod
                ndp[i+j] %= mod
    dp = ndp
    # print(dp)

ans = 0
for i in range(1, K+1):
    ans += dp[i]
    ans %= mod

print(ans)