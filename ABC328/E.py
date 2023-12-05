N, M, K = list(map(int, input().split()))
E = []
for _ in range(M):
    u, v, w = list(map(int, input().split()))
    E.append((u-1, v-1, w))

from itertools import combinations

ans = float('inf')
for selection in combinations(E, N-1):
    cost = 0
    G = [[] for _ in range(N)]
    for u, v, w in selection:
        G[u].append(v)
        G[v].append(u)
        cost += w
        cost %= K
    seen = [0]*N
    def dfs(u):
        global seen
        global G
        seen[u] = 1
        for v in G[u]:
            if seen[v]:
                continue
            dfs(v)
    dfs(0)
    if all(seen):
        ans = min(ans, cost)

print(ans)