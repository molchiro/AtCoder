# Sにコスト0の点を配置する
# 1ターンにつき1つ移動させる
# ノードは上位2点までしか持てない。
# ノードは上位2点を保持し、新しい点がくれば全体に伝搬させる

N, M = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append(b)
    G[b].append(a)
S = input()

# print(G)

nodes = [[] for _ in range(N)]
seen = [set() for _ in range(N)]
from collections import deque

dq = deque()
for i in range(N):
    if S[i] == 'S':
        nodes[i].append(0)
        dq.append((i, i, 0))
        seen[i].add(i)

while dq:
    u, origin, cost = dq.popleft()
    
    for v in G[u]:
        if origin in seen[v]:
            continue
        if len(nodes[v]) < 2:
            nodes[v].append(cost+1)
            nodes[v].sort()
            dq.append((v, origin, cost+1))
            seen[v].add(origin)
        else:
            if cost + 1 < nodes[v][-1]:
                nodes[v].pop()
                nodes[v].append(cost+1)
                nodes[v].sort()
                dq.append((v, origin, cost+1))
                seen[v].add(origin)
    # print(u, dq,seen, nodes)

# print(nodes)
for i in range(N):
    if S[i] == 'D':
        print(sum(nodes[i]))