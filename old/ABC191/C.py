H, W = list(map(int, input().split()))
grid = [[0]*W for _ in range(H)]
for h in range(H):
    row = input()
    for w in range(W):
        if row[w] == '#':
            grid[h][w] = 1

ans = 0
for h in range(H-1):
    for w in range(W-1):
        if grid[h][w] + grid[h+1][w] + grid[h][w+1] + grid[h+1][w+1] in [1, 3]:
            ans += 1
print(ans)