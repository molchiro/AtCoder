def manhattan_d(u, v):
    return abs(v[0]-u[0])+abs(v[1]-u[1])

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
      for j in range(N):
        if(dp[i][k] == INF or dp[k][j] == INF):continue
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