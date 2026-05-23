from collections import deque

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append(b)
    G[b].append(a)

dist = [0]*N
p = [-1]*N
seen = [0]*N
dq = [(0, 0)]
while dq:
    u, d = dq.pop()
    if seen[u]:
        continue

    dist[u] = d
    seen[u] = 1
    for v in G[u]:
        if seen[v]:
            continue
        p[v] = u
        dq.append((v, d+1))


leaves = []
for i in range(1, N):
    if len(G[i]) == 1:
        leaves.append((i, dist[i]))
leaves.sort(key=lambda x: (x[1], x[0]))
print(dist)
print(leaves)
print(p)

deepest_node = [(-1) for _ in range(N)]
while leaves:
    leaf, _ = leaves.pop()
    now = leaf
    while now != -1:
        if deepest_node[now] != -1:
            break
        deepest_node[now] = leaf
        now = p[now]

print(deepest_node)

for i in range(N):
    # 自身からleafの方向と、rootを経由した場合の比較
    l = dist[deepest_node[i]] - dist[i]
    r = dist[i] + dist[0]
    if deepest_node[0] == i:
        print(1)
    elif l == r:
        print(max(deepest_node[i], deepest_node[0])+1)
    elif l < r:
        print(deepest_node[0]+1)
    else:
        print(deepest_node[i]+1)