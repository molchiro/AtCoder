N, M, K = list(map(int, input().split()))
H = list(map(int, input().split()))
C = set(map(lambda x: int(x) - 1, input().split()))
order = [(i, H[i]) for i in range(N)]
order.sort(key=lambda x: x[1])
graph = [[] for _ in range(N)]

dp = [float('inf')]*N
for _ in range(M):
    A, B = list(map(lambda x: int(x) - 1, input().split()))
    if H[A] > H[B]:
        graph[A].append(B)
    else:
        graph[B].append(A)

for v, h in order:
    if v in C:
        dp[v] = 0
    else:
        if graph[v]:
            dp[v] = min([dp[x] for x in graph[v]]) + 1

for ans in dp:
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)