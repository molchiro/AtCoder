def manhattan_d(u, v):
    return abs(v[0]-u[0])+abs(v[1]-u[1])

def euclidian_d(u, v):
    return ((u[0]-v[0])**2 + (u[1]-v[1])**2)**0.5

def sign(x):
    return 0 if abs(x) == 0 else x // abs(x)

def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''
    # int.bit_count()が3.10以降はある

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f

# ワーシャル・フロイド
def warshallFloyd(graph, INF):
    N = len(graph)
    # 初期値は入力をコピー
    dp = []
    for i in range(N):
        dp.append(graph[i][:])
    
    # 3重ループで全ての頂点の間の距離を求める．
    for k in range(N):
        for i in range(N):
            if dp[i][k] == INF:
                continue
            for j in range(N):
                if dp[k][j] == INF:
                    continue
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
        
    return dp

# 拡張ユークリッドの互助法
def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

# 素因数分解
# 素数の配列を返すので、必要に応じてCounterなどを使って処理すると楽
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

# nCr 前計算ごとコピペする
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


def is_kaibun(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

def z_algorithm(s):
    """Zアルゴリズム

    Args:
        s (str): 入力文字列

    Returns:
        list: 各インデックスにおけるZ値のリスト
    """
    n = len(s)
    z = [0] * n
    z[0] = n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

from itertools import accumulate
def cumsum(input_list, mod=None, initial=None):
    func = (lambda x, y: x+y) if (mod == None) else (lambda x, y: (x+y)%mod)
    return list(accumulate(input_list, func=func, initial=initial))

def sieve_of_eratosthenes(x):
    nums = [i for i in range(x+1)]

    root = int(pow(x,0.5))
    for i in range(2,root + 1):
        if nums[i] != 0:
            for j in range(i, x+1):
                if i*j >= x+1:
                    break
                nums[i*j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes

# 2点間を通る直線の傾きと切片
def get_line_equation_from_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    a = (y2-y1)/(x2-x1)
    b = (x2*y1-x1*y2)/(x2-x1)
    return a, b

# 配列を渡すと最小増加列を返す
import bisect
def LIS(seq):
    res = [seq[0]]
    for i in range(len(seq)):
        if seq[i] > res[-1]:
            res.append(seq[i])
        else:
            res[bisect.bisect_left(res, seq[i])] = seq[i]

    return res

# 線分P1P2と線分Q1Q2の交差判定
def is_intersection(p1, p2, q1, q2):

    c1 = (p2[0] - p1[0]) * (q1[1] - p1[1]) - (p2[1] - p1[1]) * (q1[0] - p1[0])
    c2 = (p2[0] - p1[0]) * (q2[1] - p1[1]) - (p2[1] - p1[1]) * (q2[0] - p1[0])
    c3 = (q2[0] - q1[0]) * (p1[1] - q1[1]) - (q2[1] - q1[1]) * (p1[0] - q1[0])
    c4 = (q2[0] - q1[0]) * (p2[1] - q1[1]) - (q2[1] - q1[1]) * (p2[0] - q1[0])

    if c1 == 0 and c2 == 0:
        px = sorted([p1[0], p2[0]])
        qx = sorted([q1[0], q2[0]])
        py = sorted([p1[1], p2[1]])
        qy = sorted([q1[1], q2[1]])
        return (px[0] <= qx[1] and qx[0] <= px[1] and py[0] <= qy[1] and qy[0] <= py[1])

    return c1 * c2 <= 0 and c3 * c4 <= 0