N, M = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append(b)
    G[b].append(a)

W = list(map(int, input().split()))
A = list(map(int, input().split()))
# wが小さい順にdpテーブルを埋める
dp = [1]*N
for i, w in sorted(enumerate(W), key=lambda x: x[1]):
    # dp_p: 部分問題を解くdp ナップザック問題
    dp_p = [1]*(w+1)
    for to in G[i]:
        dp_p_n = dp_p[:]
        w_to = W[to]
        for x in range(w):
            dp_p_n[min(w, x+w_to)] = max(dp_p_n[min(w, x+w_to)], dp_p[x] + dp[to])
        dp_p = dp_p_n
    dp[i] = max(dp_p[:w])
# print(dp)
print(sum([a*d for a, d in zip(A, dp)]))