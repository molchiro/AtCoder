MOD = 998244353
N, M, K = list(map(int, input().split()))
ans = 1
pN = pow(2, N, MOD)
pM = pow(2, M, MOD)
print(pN, pM)
for i in range(1, K):
    tmp = ans
    ans += tmp*pN
    ans %= MOD
    ans -= tmp
    ans %= MOD
    ans += tmp*pM
    ans %= MOD
    ans -= tmp
    ans %= MOD
print(ans)