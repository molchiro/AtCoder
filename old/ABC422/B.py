H, W = list(map(int, input().split()))
field = [[0]*(W+2)] + [[0]+ [0]*W + [0] for _ in range(H)] + [[0]*(W+2)]
for h in range(H):
    C = input()
    for w in range(W):
        if C[w] == '#':
            field[h+1][w+1] = 1

f = 1
for h in range(H):
    for w in range(W):
        if field[h+1][w+1] == 1:
            if (field[h][w+1] + field[h+2][w+1] + field[h+1][w] + field[h+1][w+2]) not in [2, 4]:
                f = 0

print('Yes' if f else 'No')