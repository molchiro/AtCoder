from heapq import heappop, heappush

N, M, X, Y = list(map(int, input().split()))
X -= 1
Y -= 1

adj = [[] for _ in range(N)]
for _ in range(M):
    A, B, T, K = list(map(int, input().split()))
    A -= 1
    B -= 1
    adj[A].append((B, T, K))
    adj[B].append((A, T, K))

# print(adj)
t = [float('inf')]*N
seen = [0]*N

hq = [(0, X)]
t[X] = 0
while hq:
    v = heappop(hq)[1]
    seen[v] = 1
    for to, T, K in adj[v]:
        if seen[to]:
            continue
        tmp = t[v] + T + (K-t[v])%K
        if t[to] < tmp:
            continue
        t[to] = tmp
        heappush(hq, (tmp, to))
    # print(t)

ans = t[Y]
if ans == float('inf'):
    print(-1)
else:
    print(ans)