N = input()
D = list(map(int, input().split()))
L1, C1, K1 = list(map(int, input().split()))
L2, C2, K2 = list(map(int, input().split()))

# dp[i][j] = iまでみてAをj個使う時のBの個数の最小値
# iは１つずつ増えるので１次元で省略する
dp = [float('inf')]*1001
dp[0] = 0
for d in D:
    dp_prev = dp
    dp = [float('inf')]*1001
    # i: 今までに使ったAの個数, j: 今回使うAの個数
    for i in range(1001):
        for j in range(1001-i):
            # k: 今回使うBの個数
            k = max(0, (d-j*L1 + L2 -1)//L2)
            dp[i+j] = min(dp[i+j], dp_prev[i] + k)

# 判定
ans = float('inf')
for i in range(1001):
    if i <= K1 and dp[i] <= K2:
        ans = min(ans, C1*i + C2*dp[i])
if ans == float('inf'):
    ans = -1
print(ans)