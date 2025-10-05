mod = 998244353

def nCk(n, k):
    if k <= 1:
        return 1
    if n <= 1:
        return 1

    res = 1
    for i in range(n-k+1, n+1):
        res *= i
    for i in range(1, k+1):
        res //= i
    return res

assert nCk(4, 2) == 6
assert nCk(3, 1) == 1
assert nCk(3, 0) == 1
assert nCk(1, 1) == 1
assert nCk(0, 1) == 1

cumsum = [0]
tmp = 1
for _ in range(61):
    cumsum.append(cumsum[-1]+tmp)
    tmp *= 2
print(cumsum)


def solve(n, k, b):
    # print(n, k, b)


    if n < 0 or k < 0 or b < -1:
        return 0, 0


    if n <= 0:
        return 1, 0
    if k == 0:
        return 1, 0
    if b < 0:
        return 0, 0

    # 残り全てのビットを立ててもnを超えないなら、残りのビットからk個選んで立てる問題に変わる
    if cumsum[b+1] < n:
        return nCk(b, k), ((1<<b)*nCk(b-1, k-1) + solve(n, k, b-1)[1])%mod


    
    # a: 下位のビットが取りうるパターン数
    # b: 下位のビットによって得られる総和
    # 最上位ビットを立てる時
    a_p, b_p = solve(n-(1<<b), k-1, b-1)
    # 立てない時
    a_n, b_n = solve(n, k, b-1)
    
    res = (1<<b)*a_p
    res %= mod
    res += b_p
    res %= mod
    res += b_n
    res %= mod

    print(n, k, b, a_p+a_n, res)
    return a_p+a_n, res

T = int(input())
for _ in range(T):
    N, K = list(map(int, input().split()))
    # 最上位ビットになりうるビットを求める
    x = 0
    while 1<<(x+1) <= N:
        x += 1

    print(x, 1<<x)
    print(solve(N, K, x)[1])
    
