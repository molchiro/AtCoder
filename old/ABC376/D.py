N, M = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append(b)

from collections import deque

dq = deque()
d = [float('inf')]*N
for v in G[0]:
    dq.append(v)
    d[v] = 1

while dq:
    u = dq.popleft()
    if u == 0:
        break
    for v in G[u]:
        if d[v] == float('inf'):
            d[v] = d[u] + 1
            dq.append(v)


ans = d[0]
if ans == float('inf'):
    ans = -1
print(ans)