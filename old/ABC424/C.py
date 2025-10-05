N = int(input())

seen = [0]*N

stack = []

G = [[] for _ in range(N)]
for i in range(N):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    if (a, b) == (-1, -1):
        stack.append(i)
    G[a].append(i)
    G[b].append(i)


while stack:
    u = stack.pop()
    if seen[u] == 1:
        continue

    seen[u] = 1
    for v in G[u]:
        if seen[v] == 0:
            stack.append(v)

print(sum(seen))