N, M = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, w = list(map(lambda x: int(x) - 1, input().split()))
    w += 1
    G[a].append((b, w))

seen = [[0]*1024 for _ in range(N)]
stack = []
stack.append((0, 0))
while stack:
    u, x = stack.pop()
    if seen[u][x]:
        continue
    seen[u][x] = 1

    for v, w in G[u]:
        y = x^w
        if seen[v][y]:
            continue
        stack.append((v, y))

ans = float('inf')
for i in range(1024):
    if    seen[N-1][i] == 1:
        ans = min(ans, i)
if ans == float('inf'):
    ans = -1
print(ans)