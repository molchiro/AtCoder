INF = 10**18

N, K = list(map(int, input().split()))
double = [[list(map(int, input().split())) for _ in range(N)]]

for _ in range(30):
    tmp = [[INF]*N for _ in range(N)]
    # iを出発してjを経由してkに行く
    for d in range(N):
        for j in range(N):
            for k in range(N):
                tmp[d][k] = min(tmp[d][k], double[-1][d][j] + double[-1][j][k])
    double.append(tmp)

# print(*double, sep='\n')

# 最初iにいて今jにいるためのコスト
ans = [[INF]*N for _ in range(N)]
for d in range(N):
    ans[d][d] = 0
# print(ans)
# exit()
for d in range(30):
    if K%2:
        nxt = [[INF]*N for _ in range(N)]

        # 最初iにいて、jを経由して、kに移動するコスト
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    nxt[i][k]= min(nxt[i][k], ans[i][j] + double[d][j][k])
        ans = nxt[:][:]
    K //= 2

# print(*ans, sep='\n')

for d in range(N):
    print(ans[d][d])