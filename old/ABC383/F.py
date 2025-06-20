from copy import deepcopy

N, X, K = list(map(int, input().split()))
items = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*2 for _ in range(X+1)]
prev = -1
for p, u, c in sorted(items, key=lambda x: x[2]):
    if c != prev:
        for x in range(X+1):
            dp[x][0] = max(dp[x])
            dp[x][1] = 0

    for x in range(X-p, -1, -1):
        dp[x+p][1] = max(dp[x+p][1], dp[x][0]+u+K, dp[x][1]+u)
    
    prev = c

ans = 0
for a, b in dp:
    ans = max(ans, a, b)

print(ans)