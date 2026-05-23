N, M = list(map(int, input().split()))

G = [[] for _ in range(N)]
for _ in range(M):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append(b)

seen = [0]*N

from collections import deque

dq = deque()

dq.append(0)

while dq:
    u = dq.popleft()

    if seen[u]:
        continue

    seen[u] = 1

    for v in G[u]:
        if seen[v]:
            continue

        dq.append(v)

print(sum(seen))