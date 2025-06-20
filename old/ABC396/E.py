from atcoder.dsu import DSU
N, M = list(map(int, input().split()))
dsu = DSU(N)
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, w  = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append((b, w+1))
    G[b].append((a, w+1))
    dsu.merge(a, b)

from collections import deque

bit = [[-1]*30 for _ in range(N)]
groups = dsu.groups()
for k in range(30):
    for group in groups:
        ct = 0
        dq = deque([group[0]])
        bit[group[0]][k] = 0
        while dq:
            u = dq.popleft()
            for v, w in G[u]:
                if bit[v][k] == -1:
                    bit[v][k] = ((w >> k) & 1) ^ bit[u][k]
                    if bit[v][k] == 1:
                        ct += 1
                    dq.append(v)
                else:
                    if bit[v][k] != ((w >> k) & 1) ^ bit[u][k]:
                        print(-1)
                        exit()
        
        if ct > len(group)//2:
            for u in group:
                bit[u][k] = (bit[u][k]+1)%2

    # print(bit)

ans = []
for i in range(N):
    tmp = 0
    for k in range(30):
        if bit[i][k]:
            tmp += 1 << k
    ans.append(tmp)
print(*ans)
            


