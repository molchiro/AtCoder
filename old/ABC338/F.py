N, M = list(map(int, input().split()))
# ワーシャルフロイドで全頂点間の最短距離を求める
INF = 10**18
d = [[INF]*N for _ in range(N)]
for _ in range(M):
    U, V, W = list(map(int, input().split()))
    d[U-1][V-1] = W
for k in range(N):
    for i in range(N):
        for j in range(N):
            if d[i][k] != INF and d[k][j] != INF:
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
# print(d)

# dp[S][i]: Sに行ったことがあり、今iにいる
dp = [[INF]*N for _ in range(2**N)]
for i in range(N):
    dp[1<<i][i] = 0

for s in range(2**N):
    for i in range(N):
        # INFからは遷移しない
        if dp[s][i] == INF:
            continue
        # sとiの組み合わせに矛盾がある時はスキップ
        if not s >> i & 1:
            continue
        for j in range(N):
            if d[i][j] == INF:
                continue
            new_s = s | 1 << j
            dp[new_s][j] = min(dp[new_s][j], dp[s][i] + d[i][j])
# print(dp)
ans = min(dp[-1])
if ans == INF:
    print('No')
else:
    print(ans)