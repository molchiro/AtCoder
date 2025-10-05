N, M = list(map(int, input().split()))
edges_set = set()
edges = [None]*M
G = [set() for _ in range(N)]
for i in range(M):
    u, v = list(map(lambda x: int(x) - 1, input().split()))
    edges[i] = (u, v)
    edges_set.add((u, v))
    G[u].add(v)

from atcoder.dsu import DSU
dsu = DSU(N)

Q = int(input())
X = list(map(lambda x: int(x) - 1, input().split()))
ans = M
for x in X:
    if edges[x] == None:
        print(ans)
        continue

    u, v = edges[x]
    edges[x] = None
    u_leader = dsu.leader(u)
    v_leader = dsu.leader(v)