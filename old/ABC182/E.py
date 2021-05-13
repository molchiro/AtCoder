H, W, N, M = list(map(int, input().split()))
lights = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]
blocks = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

grid = [['']*W for _ in range(H)]

for h, w in blocks:
    grid[h][w] = 'B'

for h, w in lights:
    grid[h][w] = 'RC'
    # 右
    dw = 1
    while w+dw < W:
        if grid[h][w+dw] in ['B', 'C', 'RC', 'CR']:
            break
        grid[h][w+dw] += 'C'         
        dw += 1
    # 左
    dw = -1
    while w+dw >= 0:
        if grid[h][w+dw] in ['B', 'C', 'RC', 'CR']:
            break
        grid[h][w+dw] += 'C'
        dw -= 1
    # 下
    dh = 1
    while h+dh < H:
        if grid[h+dh][w] in ['B', 'R', 'RC', 'CR']:
            break
        grid[h+dh][w] += 'R'
        dh += 1
    # 上
    dh = -1
    while h+dh >= 0:
        if grid[h+dh][w] in ['B', 'R', 'RC', 'CR']:
            break
        grid[h+dh][w] += 'R'
        dh -= 1
ans = H*W
for h in range(H):
    for w in range(W):
        if grid[h][w] in ['', 'B']:
            ans -= 1
print(ans)