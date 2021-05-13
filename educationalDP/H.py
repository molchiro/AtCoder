mod = 10**9 + 7
H, W = list(map(int, input().split()))
grid = [[1]*W for _ in range(H)]
for h in range(H):
    row = input()
    for w in range(W):
        if row[w] == '#':
            grid[h][w] = 0

dp = [[0]*W for _ in range(H)]

# initialize
dp[0][0] = 1
for h in range(1, H):
    if grid[h][0]:
        dp[h][0] = dp[h-1][0]
for w in range(1, W):
    if grid[0][w]:
        dp[0][w] = dp[0][w-1]

# solve
for h in range(1, H):
    for w in range(1, W):
        if grid[h][w]:
            dp[h][w] = (dp[h-1][w] + dp[h][w-1])%mod
print(dp[-1][-1])