from itertools import product
from copy import deepcopy

H, W, K = list(map(int, input().split()))
board = [list(input()) for _ in range(H)]

ans = 0
for row in product(['.', '%'], repeat=H):
    if row == tuple(['%']*H):
        continue
    tmp1 = deepcopy(board)
    for h in range(H):
        if row[h] == '%':
            tmp1[h] = ['%']*W
    for col in product(['.', '%'], repeat=W):
        if col == tuple(['%']*W):
            continue
        tmp2 = deepcopy(tmp1)
        for w in range(W):
            if col[w] == '%':
                for h in range(H):
                    tmp2[h][w] = '%'
        if sum(tmp2, []).count('#') == K:
            ans += 1
print(ans)
