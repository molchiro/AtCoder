from collections import deque

T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = list(map(lambda x: int(x) - 1, input().split()))
        G[a].append(b)
        G[b].append(a)

    dist = [None]*N
    dist[0] = 0

    p = [None]*N

    dq = deque()
    dq.append((0, 0))
    f = 0

    while dq:
        u, d = dq.pop()
        dist[u] = d

        for v in G[u]:
            if v == p[u]:
                continue

            if dist[v] == None:
                # dist[v] = dist[u] + 1
                dq.append((v, d+1))
                p[v] = u
            else:
                if (dist[v]-dist[u])%2 == 0:
                    s = u
                    g = v
                    f = 1
                    break

        else:
            continue

        break

    # print(p, s, g)

    if f:
        ans = [s+1]
        now = s
        while now != g:
            now = p[now] 
            ans.append(now+1)

        print(len(ans))
        print(*ans)

    else:
        print(-1)