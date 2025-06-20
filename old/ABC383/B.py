from copy import deepcopy

H, W, D = list(map(int, input().split()))
D += 1
field = [[-1]*(W+2)] + [[-1]+ [0]*W + [-1] for _ in range(H)] + [[-1]*(W+2)]
for h in range(H):
    S = input()
    for w in range(W):
        if S[w] == '#':
            field[h+1][w+1] = 1

# print(*field, sep='\n')

def move(x, y):
    return [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]

from collections import deque

def culc(a, b):
    global H, W, D
    global field
    f = deepcopy(field)
    dq = deque()
    dq.append((a[0], a[1], D))
    dq.append((b[0], b[1], D))
    while dq:
        h, w, d = dq.popleft()

        if f[h][w] > d:
            continue

        f[h][w] = d

        if d-1 == 0:
            continue
        
        for h_n, w_n in move(h, w):
            if f[h_n][w_n] == -1:
                continue

            dq.append((h_n, w_n, d-1))

    res = 0
    for h in range(H+2):
        for w in range(W+2):
            if f[h][w] > 0 and field[h][w] == 0:
                res += 1

    # print(*f, sep='\n')
    # print()
    return res

ans = 0
for h1 in range(1, H+2):
    for w1 in range(1, W+2):
        if field[h1][w1] != 0:
            continue
        for h2 in range(1, H+2):
            for w2 in range(1, W+2):
                if field[h2][w2] != 0:
                    continue
                if h1 == h2 and w1 == w2:
                    continue
                ans = max(ans, culc([h1, w1], [h2, w2]))
print(ans)
