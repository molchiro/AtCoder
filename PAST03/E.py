N, M, Q = list(map(int, input().split()))
to = [[] for _ in range(N)]
for _ in range(M):
    u, v = list(map(lambda x: int(x) - 1, input().split()))
    to[u].append(v)
    to[v].append(u)
color = list(map(int, input().split()))

for _ in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        x = s[1] - 1
        c = color[x]
        print(c)
        for neighbor in to[x]:
            color[neighbor] = c
    else:
        x = s[1] - 1
        y = s[2]
        print(color[x])
        color[x] = y