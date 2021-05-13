N = int(input())
cities = [list(map(int, input().split())) for _ in range(N)]

d = [[0]*N for _ in range(N)]
for s in range(N):
    for t in range(N):
        a, b, c = cities[s]
        p, q, r = cities[t]
        d[s][t] = abs(p-a) + abs(q-b) + max(0, r-c)

dp = [[float('inf')]*N for i in range(1 << N)]
dp[0][0] = 0

for S in range(1 << N):
    for t in range(N):
        if not S & (1 << t):
            continue
        for s in range(N):
            dp[S][t] = min(dp[S][t], dp[S - (1 << t)][s] + d[s][t])

print(dp[-1][0])