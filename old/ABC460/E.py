from math import gcd

mod = 998244353

T = int(input())
for _ in range(T):
    ans = 0
    N, M = list(map(int, input().split()))
    # yが取りうる全ての桁を全探索
    for d in range(1, len(str(N))):
        z = int('9'*d)
        g = gcd(z, M)
        M_ = M//g
        tmp = (N//M_) * (9*(10**(d-1)))
        tmp %= mod
        # tmp -= int('9'*d)//M_ - (10**d//M_)
        # tmp %= mod

        # print(d, z, g, M_, tmp)

        ans += tmp
        ans %= mod

    # 最後の桁は同じような別計算
    d = len(str(N))
    z = int('9'*d)
    g = gcd(z, M)
    M_ = M//g
    tmp = (N//M_) * (N - (int('9'*(d-1)) if d > 1 else 0))
    tmp %= mod
    # print(tmp)
    # tmp -= N//M_ - (10**d//M_)
    # tmp %= mod

    # print(d, z, g, M_, tmp)

    ans += tmp
    ans %= mod

    print(ans)