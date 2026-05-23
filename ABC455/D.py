N, Q = list(map(int, input().split()))

parent = [-1]*N
child = [-1]*N

query = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(Q)]

while query:
    C, P = query.pop()

    if parent[C] == -1:
        parent[C] = P
        child[P] = C


# print(parent)
# print(child)


roots = []
for i in range(N):
    if parent[i] == -1 and child[i] != -1:
        roots.append(i)

ans = [1]*N
for r in roots:
    now = r
    while child[now] != -1:
        c = child[now]
        ans[r] += 1
        ans[c] = 0
        now = c

print(*ans)