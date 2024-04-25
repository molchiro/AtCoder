def manhattan_d(u, v):
    return abs(v[0]-u[0])+abs(v[1]-u[1])

def sign(x):
    return 0 if abs(x) == 0 else x // abs(x)

def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

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