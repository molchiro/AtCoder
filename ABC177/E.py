# 入力
N = int(input())
A = list(map(int, input().split()))

R = max(A)

# D[x]にxを割り切れる最初の素数を格納
# 次に行う素因数分解で試し割りのムダを削減するための前準備
D = [0]*(R+1)
for i in range(2, R+1):
    if D[i]:
        continue
    n = i
    while n < R+1:
        if D[n] == 0:
            D[n] = i
        n += i

# 素因数分解し、素因子をカウント
# ex: 12 => 2と3のカウントを+1する
prime_factor_counter = [0]*(R+1)
for a in A:
    tmp = a
    while tmp > 1:
        prime_factor = D[tmp]
        prime_factor_counter[prime_factor] += 1
        while tmp%prime_factor == 0:
            tmp //= prime_factor

# 回答出力
if max(prime_factor_counter) < 2:
    print('pairwise coprime')
elif max(prime_factor_counter) - A.count(1) < N:
    print('setwise coprime')
else:
    print('not coprime')