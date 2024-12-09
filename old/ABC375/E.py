N = int(input())
# dp[x][y]: i番目の人まで見た時、チーム1に所属する人の強さの和をx, チーム2に所属する人の強さの和をyとした時の所属チームを変更した人の人数の最小値
dp = [[float('inf')]*502 for _ in range(502)]
dp[0][0] = 0
accum = 0

for _ in range(N):
    ndp = [[float('inf')]*502 for _ in range(502)]
    A, B = list(map(int, input().split()))
    accum += B
    for i in range(502):
        for j in range(502):
            # xに所属させる
            ndp[min(501, i+B)][j] = min(ndp[min(501, i+B)][j], dp[i][j] + (0 if A == 1 else 1))
            # yに所属させる
            ndp[i][min(501, j+B)] = min(ndp[i][min(501, j+B)], dp[i][j] + (0 if A == 2 else 1))
            # zに所属させる
            ndp[i][j] = min(ndp[i][j], dp[i][j] + (0 if A == 3 else 1))


    dp = ndp

if accum%3 == 0:
    ans = dp[accum//3][accum//3]
    if ans == float('inf'):
        ans = -1
    print(ans)
else:
    print(-1)