N, K = list(map(int, input().split()))

# 合計点がk点になる場合の数を準備
# dp[i][k] = 場合の数
# i: 1~Nの整数を何回選んだか
# k: 合計点
# dp[i][k] = dp[i-1][k-1] + dp[i-1][k-2]+ ... +dp[k-N]
dp = [[0]*(3*N+1) for _ in range(4)]
# １回目
for k in range(1, N+1):
    dp[1][k] = 1
# ２回目
accum = [0]*(3*N+2)
for k in range(1, 3*N+1):
    accum[k] = accum[k-1] + dp[1][k]
for k in range(1, 2*N+1):
    dp[2][k] = accum[k-1] - accum[max(0, k-N-1)]
# ３回目
accum = [0]*(3*N+2)
for k in range(1, 3*N+1):
    accum[k] = accum[k-1] + dp[2][k]
for k in range(1, 3*N+1):
    dp[3][k] = accum[k-1] - accum[max(0, k-N-1)]

# K番目が合計点が何点の群に含まれるか判断
k = 3
while K > dp[3][k]:
    K -= dp[3][k]
    k += 1
# 合計点がkである組み合わせを並びが若い順にK個分シミュレーション
i = 0
for a in range(1, min(N, k)+1):
    b_min = max(1, k-a-N)
    b_max = min(N, k-a-1)
    if b_max-b_min+1 < K:
        K -= max(0, b_max-b_min+1)
    else:
        b = b_min + K - 1
        c = k-a-b
        print(a, b, c)
        exit()
