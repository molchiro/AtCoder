from collections import deque

N = int(input())
graph = [[] for _ in range(N)]
edges = []
for _ in range(N-1):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    edges.append((a, b))
    graph[a].append(b)
    graph[b].append(a)

parent = [-1]*N

d = deque([(0, -1)])
while d:
    v, p = d.popleft()
    parent[v] = p
    for u in graph[v]:
        if u == p:
            continue
        d.append((u, v))

Q = int(input())

imos = [0]*N
c = 0
for _ in range(Q):
    t, e, x = list(map(int, input().split()))
    e -= 1
    a, b = edges[e]
    if t == 2:
        a, b = b, a
    if parent[a] == b:
        imos[a] += x
    else:
        imos[b] -= x
        c += x

nodes = [0]*N
d = deque([(0, -1, c)])
while d:
    v, p, c = d.popleft()
    c += imos[v]
    nodes[v] = c
    for u in graph[v]:
        if u == p:
            continue
        d.append((u, v, c))

print(*nodes, sep='\n')