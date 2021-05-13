R, C, K = list(map(int, input().split()))
value = [[0]*C for _ in range(R)]
# 価値テーブルの作成
for i in range(K):
    r, c, v = list(map(int, input().split()))
    value[r-1][c-1] = v
# dp<n>[行][列] = その列でn個取ったときの価値の最大値
dp0 = [[0]*(C+1) for _ in range(R+1)]
dp2 = [[0]*(C+1) for _ in range(R+1)]
dp1 = [[0]*(C+1) for _ in range(R+1)]
dp3 = [[0]*(C+1) for _ in range(R+1)]
# print(dp0)
for r in range(1, R+1):
    for c in range(1, C+1):
        # print(r, c)
        v = value[r-1][c-1]
        dp0[r][c] = max(dp0[r-1][c], dp1[r-1][c], dp2[r-1][c], dp3[r-1][c], dp0[r][c-1])
        dp1[r][c] = max(dp1[r][c-1], dp0[r-1][c] + v, dp1[r-1][c] + v,dp2[r-1][c] + v, dp3[r-1][c] + v, dp0[r][c-1] + v)
        dp2[r][c] = max(dp2[r][c-1], dp1[r][c-1] + v)
        dp3[r][c] = max(dp3[r][c-1], dp2[r][c-1] + v)
print(max(dp0[R][C], dp1[R][C], dp2[R][C], dp3[R][C]))