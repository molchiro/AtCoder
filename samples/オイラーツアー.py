import sys
sys.setrecursionlimit(10**9)

N = int(input())
edges = []
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    edges.append((a, b))
    G[a].append(b)
    G[b].append(a)

# オイラーツアー
tour = []
in_out = [[None, None] for _ in range(N)]
seen = [0]*N

def dfs(u):
    global N, G
    global tour, in_out, seen

    seen[u] = 1
    in_out[u][0] = len(tour)
    tour.append(u)

    for v in G[u]:
        if seen[v]:
            continue
        seen[v] = 1
        dfs(v)

    in_out[u][1] = len(tour)    

dfs(0)