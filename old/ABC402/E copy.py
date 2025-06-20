N, X = list(map(int, input().split()))
problems = [list(map(int, input().split())) for _ in range(N)]

# dp[x][s] : 残りのお金がx円の時の期待値の最大値 状態j
dp = [[0]*(X+1) for _ in range(1<<N+1)]

# print(dp)

# 残り円
for x in range(X+1):
    # 状態j
    for j in range(1<<N):
        # どの問題に挑戦するのが最適か
        gain = 0
        for i in range(N):
            s, c, p = problems[i]
            # 予算オーバー
            if x-c < 0:
                continue
            # すでに解いている
            if (j >> i) & 1:
                continue

            gain = max(gain, (dp[j+(1<<i)][x-c] + s)*p/100 + dp[j][x-c]*(100-p)/100)
        dp[j][x] = gain

print(dp[0][X])
