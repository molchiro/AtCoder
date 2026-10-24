from collections import deque

T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = list(map(lambda x: int(x) - 1, input().split()))
        G[a].append(b)
        G[b].append(a)
    
    ans = [-1]*N
    ans[0] = 0
    dq = deque()
    if N > 1:
        dq.append(0)
    while dq:
        u = dq.pop()
        if ans[u] > 0:
            continue
        ans[u] = max([ans[v] for v in G[u]]) + 1
        for v in G[u]:
            if ans[v] > -1:
                continue
            dq.append(v)
    
    print(*ans)