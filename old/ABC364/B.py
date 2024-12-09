H, W = list(map(int, input().split()))
now = tuple(list(map(int, input().split())))

field = [[-1]*(W+2)] + [[-1]+ [0]*W + [-1] for _ in range(H)] + [[-1]*(W+2)]
for h in range(H):
    C = input()
    for w in range(W):
        if C[w] == '#':
            field[h+1][w+1] = -1

# U, D, R, Lを渡して移動後の座標を返す
def walk(now, direction):
    h, w = now
    walk_map = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    dh, dw = walk_map[direction]
    return (h+dh, w+dw)

for x in input():
    h, w = walk(now, x)
    if field[h][w] == 0:
        now = (h, w)

print(*now)