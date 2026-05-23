N, M, L, S, T = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append((b, c+1))

dp = [(0, 0)]
for _ in range(L):
    ndp = []
    for u, total in dp:
        for v, c in G[u]:
            n_total = total + c
            if n_total <= T:
                ndp.append((v, n_total))

    dp = ndp
    # print(dp)

ans = set()
for u, total in dp:
    if S <= total <= T:
        ans.add(u+1)
print(*sorted(list(ans)))