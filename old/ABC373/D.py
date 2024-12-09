N, M = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, w = list(map(lambda x: int(x) - 1, input().split()))
    w += 1
    G[a].append((b, w))
    G[b].append((a, -w))

import sys
sys.setrecursionlimit(10**9)

ans = [None]*N

from collections import deque

dq = deque()

for i in range(N):
    if ans[i] != None:
        continue

    ans[i] = 0
    dq.append(i)
    while dq:
        u = dq.pop()
        for v, w in G[u]:
            if ans[v] != None:
                continue

            ans[v] = ans[u]+w
            dq.append(v)

print(*ans)
