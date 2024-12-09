N = int(input())

G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append(b)
    G[b].append(a)

from atcoder.dsu import DSU

dsu = DSU(N)

# 次数3のノード同士を連結する

for u in range(N):
    if len(G[u]) != 3:
        continue

    for v in G[u]:
        if len(G[v]) == 3:
            dsu.merge(u, v)


# print(G)

# 次数2のノードの数を記録する
two_nodes = [0]*N
for u in range(N):
    if len(G[u]) != 3:
        continue

    leader = dsu.leader(u)
    # print(u, leader)
    for v in G[u]:
        if len(G[v]) == 2:
            two_nodes[leader] += 1

# print(two_nodes)

# 答えを計算
ans = 0
for n in two_nodes:
    ans += n*(n-1)//2
print(ans)