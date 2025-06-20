H, W, X, Y = list(map(int, input().split()))
field = [[-1]*(W+2)] + [[-1]+ [0]*W + [-1] for _ in range(H)] + [[-1]*(W+2)]
houses = set()
for h in range(H):
    C = input()
    for w in range(W):
        if C[w] == '#':
            field[h+1][w+1] = -1
        elif C[w] == '@':
            houses.add((h+1, w+1))


# U, D, R, Lを渡して移動後の座標を返す
def walk(now, direction):
    h, w = now
    walk_map = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    dh, dw = walk_map[direction]
    return (h+dh, w+dw)

now = (X, Y)
seen = set()
for d in input():
    n_h, n_w = walk(now, d)
    if field[n_h][n_w] == -1:
        continue

    now = (n_h, n_w)
    if now in houses:
        seen.add(now)
    
    # print(now)

print(now[0], now[1], len(seen))