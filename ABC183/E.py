mod = 10**9+7
H, W = list(map(int, input().split()))
field = [[0]*W + [-1] for _ in range(H)] + [[-1]*(W+1)]

for h in range(H):
    S = input()
    for w in range(W):
        if S[w] == '#':
            field[h][w] = -1

field[0][0] = 1
for h in range(H):
    for w in range(W):
        tmp = field[h][w]
        if tmp == -1:
            continue
        # 右
        for i in range(1, 2000):
            if field[h][w+i] == -1:
                break
            field[h][w+i] += tmp
            field[h][w+i] %= mod
        # 右下
        for i in range(1, 2000):
            if field[h+i][w+i] == -1:
                break
            field[h+i][w+i] += tmp
            field[h+i][w+i] %= mod
        # 下
        for i in range(1, 2000):
            if field[h+i][w] == -1:
                break
            field[h+i][w] += tmp
            field[h+i][w] %= mod
        # print(*field, sep='\n')
        # print()

print(field[H-1][W-1])
