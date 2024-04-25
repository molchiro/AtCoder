from collections import deque


N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = list(map(lambda x: int(x) - 1, input().split()))
    G[u].append(v)
    G[v].append(u)

seen = [0]*N
seen[0] = 1
def solve(s):

    dq = deque([(s, 0)])
    res = 0
    while dq:
        u, d = dq.popleft()
        if seen[u]:
            continue
        seen[u] = 1
        res += 1
        for v in G[u]:
            if seen[v] == 0:
                dq.appendleft((v, d+1))
    return res + 1


print(N - max([solve(v) for v in G[0]]) + 1)