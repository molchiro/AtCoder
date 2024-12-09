from itertools import chain

H, W = 8, 8

field = [[0]*(W+2)] + [[0]+ [1]*W + [0] for _ in range(H)] + [[0]*(W+2)]

def check(h, w):
    global field, H, W

    for i in range(8):
        field[i+1][w+1] = 0
        field[h+1][i+1] = 0

for h in range(8):
    row = input()
    for w in range(8):
        if row[w] == '#':
            check(h, w)

print(sum(chain.from_iterable(field)))