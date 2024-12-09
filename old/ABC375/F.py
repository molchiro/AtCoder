N, M, Q = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]
queries = [list(map(int, input().split())) for _ in range(Q)]

# クエリは逆順で処理する
# queries = queries[::-1]

initial_edges = []
disabled = [0]*M
for i in range(Q-1, -1, -1):
    q = queries[i]
    if q[0] == 1:
        disabled[q[1]-1] = 1

INF = float('inf')


# 全点間距離
dist = [[INF] * N for _ in range(N)]
for i in range(N):
    dist[i][i] = 0  # 自分自身への距離は0

for m in range(M):
    if disabled[m]:
        continue
    u, v, w = edges[m]
    dist[u-1][v-1] = w
    dist[v-1][u-1] = w

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 新しい辺の追加を処理
def add_edge(u, v, w):
    global dist, N
    # 新しい辺(u, v)を追加（双方向）
    if dist[u][v] > w:
        dist[u][v] = w
        dist[v][u] = w

        # 新しい辺の影響を反映させるためにフロイドワーシャルを部分的に更新
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][u] + dist[u][v] + dist[v][j], dist[i][v] + dist[v][u] + dist[u][j])




ans = []
for i in range(Q-1, -1, -1):
    q = queries[i]
    if q[0] == 1:
        u, v, w = edges[q[1]-1]
        add_edge(u-1, v-1, w)
    else:
        _, x, y = q
        
        a = dist[x-1][y-1]
        if a == INF:
            a = -1
        ans.append(a)

for i in range(len(ans)-1, -1, -1):
    print(ans[i])