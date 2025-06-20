import sys
sys.setrecursionlimit(10**8)

N = int(input())
X = list(map(int, input().split()))

G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, w = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append((b, w+1))
    G[b].append((a, w+1))

ans = 0
seen = [0]*N
seen[0] = 1
def dfs(u=0):
    global N, X, G, ans

    for v, w in G[u]:
        if seen[v]:
            continue

        seen[v] = 1
        dfs(v)

        ans += w*abs(X[v])
        X[u] += X[v]
        X[v] = 0

dfs()
print(ans)