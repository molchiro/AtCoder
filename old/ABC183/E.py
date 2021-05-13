mod = 10**9+7
H, W = list(map(int, input().split()))
field = []

for h in range(H):
    field.append(input())

dp = [[0]*(W+1) for _ in range(H+1)]
x_accum = [[0]*(W+1) for _ in range(H+1)]
y_accum = [[0]*(W+1) for _ in range(H+1)]
d_accum = [[0]*(W+1) for _ in range(H+1)]
dp[1][1] = 1
for h in range(1, H+1):
    for w in range(1, W+1):
        if field[h-1][w-1] == '#':
            dp[h][w] = 0
            x_accum[h][w] = 0
            y_accum[h][w] = 0
            d_accum[h][w] = 0
        else:
            dp[h][w] += x_accum[h][w-1] + y_accum[h-1][w] + d_accum[h-1][w-1]
            dp[h][w] %= mod
            x_accum[h][w] += x_accum[h][w-1] + dp[h][w]
            y_accum[h][w] += y_accum[h-1][w] + dp[h][w]
            d_accum[h][w] += d_accum[h-1][w-1] + dp[h][w]
# print(*dp, sep='\n')
print(dp[H][W])