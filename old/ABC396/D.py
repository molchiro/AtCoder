N, M = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, w = list(map(lambda x: int(x) - 1, input().split()))
    w += 1
    G[a].append((b, w))
    G[b].append((a, w))

paths = []
stack = []

stack.append((0, [], set())) # u, w_list, seen
while stack:
    # print(stack)
    u, w_list, seen = stack.pop()
    seen.add(u)
    if u == N-1:
        paths.append(w_list[:])
    for v, w in G[u]:
        if v in seen:
            continue

        stack.append((v, w_list[:]+[w], seen.copy()))

# print(paths)

ans = float('inf')
for path in paths:
    tmp = 0
    for w in path:
        tmp ^= w
    ans = min(ans, tmp)

print(ans)
