N, M = list(map(int, input().split()))
INF = 10**18
# 超頂点「上空」を設定することで空港同士の直接結合によるN^2辺をN辺に減らす

dist = [[INF]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    dist[i][i] = 0

for _ in range(M):
    A, B, C = list(map(int, input().split()))
    A -= 1
    B -= 1
    dist[A][B] = min(dist[A][B], C)
    dist[B][A] = min(dist[B][A], C)

K, T = list(map(int, input().split()))
D = list(map(lambda x: int(x) - 1, input().split()))
for d in D:
    dist[d][N] = T
    dist[N][d] = 0

# ワーシャルフロイドで全点間距離を求める
for w in range(N+1):
    for u in range(N+1):
        if dist[u][w] == INF:
            continue
        for v in range(N+1):
            if dist[w][v] == INF:
                continue
            tmp = dist[u][w] + dist[w][v]
            if tmp < dist[u][v]:
                dist[u][v] = tmp

                
ans = 0
for i in range(N):
    for j in range(N):
        if dist[i][j] == INF:
            continue
        ans += dist[i][j]

# print(dist)

Q = int(input())
added_edges = []
for _ in range(Q):
    query = input()
    if query == '3':
        added_edges.sort(key=lambda x: x[2])
        for u, v, d in added_edges:
            if dist[u][v] <= d:
                continue
            for i in range(N+1):
                if dist[i][u] == INF:
                    continue
                for j in range(N+1):
                    if dist[i][u] + d + dist[v][j] < dist[i][j]:
                        if dist[i][j] == INF:
                            if N not in [i, j]:
                                ans += dist[i][u] + d + dist[v][j]
                            dist[i][j] = dist[i][u] + d + dist[v][j]
                        else:
                            if N not in [i, j]:

                                ans -= dist[i][j] - (dist[i][u] + d + dist[v][j])
                            dist[i][j] = dist[i][u] + d + dist[v][j]

        print(ans)
        added_edges = []
    else:
        t, *remainding = query.split()
        if t == '1':
            x, y, t = list(map(int, remainding))
            added_edges.append((x-1, y-1, t))
            added_edges.append((y-1, x-1, t))
        else:
            x = int(remainding[0])-1
            added_edges.append((x, N, T))
            added_edges.append((N, x, 0))
        
        

