N, M = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    G[b].append(a)

ok = [0]*N

Q = int(input())
for _ in range(Q):
    t, v = list(map(lambda x: int(x) - 1, input().split()))
    if t == 0:
        stack = [v]
        while stack:
            u = stack.pop()
            if ok[u]:
                continue
            ok[u] = 1
            for v in G[u]:
                if ok[v] == 0:
                    stack.append(v)
    else:
        print('Yes' if ok[v] else 'No')
