from atcoder.dsu import DSU

N, M = list(map(int, input().split()))
edges = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
if N != M:
    print('No')
    exit()

G = [[] for _ in range(N)]
dsu = DSU(N)
for u, v in edges:
    G[u].append(v)
    G[v].append(u)
    dsu.merge(u, v)

print('Yes' if len(dsu.groups()) == 1 and all([len(to) == 2 for to in G]) else 'No')