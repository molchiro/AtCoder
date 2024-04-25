H, W, N = list(map(int, input().split()))
field = [['.']*W for _ in range(H)]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
now = (0, 0)
dirs_idx = 0
for _ in range(N):
    h, w = now
    if field[h][w] == '.':
        field[h][w] = '#'
        dirs_idx += 1
        dirs_idx %= 4
        now = ((h+dirs[dirs_idx][0])%H, (w+dirs[dirs_idx][1])%W)
    else:
        field[h][w] = '.'
        dirs_idx -= 1
        dirs_idx %= 4
        now = ((h+dirs[dirs_idx][0])%H, (w+dirs[dirs_idx][1])%W)

for h in range(H):
    print(''.join(field[h]))