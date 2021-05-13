digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D' , 'E', 'F']
MOD = 10**9+7

N, K = input().split()
K = int(K)

# dp[i][j][f]
# i: 先頭からi文字目
# j: j種類の文字を使った(0文字から初めて、あり得ないが17文字まで作っておく)
# f: Nの上限ギリギリフラグ
dp = [[[0]*2 for _ in range(18)] for _ in range(len(N)+1)]

for i in range(1, len(N)+1):
    dp[i][0][0] = 1
dp[0][0][1] = 1

seen = set()
for i in range(1, len(N)+1):
    Ni = N[i-1]
    n = len(seen)
    # i桁目までがNと同じの状態のまま遷移
    inc = 0 if Ni in seen else 1
    dp[i][n+inc][1] += dp[i-1][n][1]

    # i桁目までがNと同じの状態からN以下が確定する遷移
    for j in range(digits.index(Ni)):
        inc = 0 if digits[j] in seen else 1
        dp[i][n+inc][0] += dp[i-1][n][1]
    seen.add(Ni)

    # N以下であることが確定した状態から遷移
    for j in range(17):
        dp[i][j+1][0] += dp[i-1][j][0]*(16-j)
        dp[i][j][0] += dp[i-1][j][0]*j
    # 先頭が0のものをカウントしているため取り除く
    dp[i][1][0] -= 1

    # MODをとる
    for j in range(17):
        dp[i][j+1][0] %= MOD
        dp[i][j][0] %= MOD
        dp[i][j+1][1] %= MOD
        dp[i][j][1] %= MOD
        
ans = dp[len(N)][K][0] + dp[len(N)][K][1]
ans %= MOD
print(ans)