# nCr 前計算ごとコピペする
mod = 998244353
N = 200001  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)

def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % mod


N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = [(a*a)%mod for a in A]

if N == 1:
    print((A[0]**2)%mod)
else:
    if K == 1:
        ans = sum(B)%mod
    elif K == N:
        ans = (sum(A)%mod)**2
        ans %= mod
    else:
        ans = ((sum(A)%mod)**2) * cmb(N-2, K-2)
        ans %= mod
        # print(ans)
        ans += (sum(B)%mod) * cmb(N-2, K-1)
        ans %= mod

    print(ans)