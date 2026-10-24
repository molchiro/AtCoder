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

# print(seen)
# print(tour)
# print(in_out)

size = [e[1]-e[0] for e in in_out]
# print(size)

imos = [0]*(N+1)

for i, (u, v) in enumerate(edges, start=1):
    if size[u] > size[v]:
        p, c = u, v
    else:
        p, c = v, u

    # 子の方が大きいなら行きがけに足して帰りがけに減らす
    if size[c] > N//2:
        imos[in_out[c][0]] += i
        imos[in_out[c][1]] -= i
    else:
        imos[0] += i
        imos[-1] -= i
        imos[in_out[c][0]] -= i
        imos[in_out[c][1]] += i

for i in range(N):
    imos[i+1] += imos[i]
# print(imos)

ans = [None]*N
for i in range(N):
    ans[tour[i]] = imos[i]
print(*ans)