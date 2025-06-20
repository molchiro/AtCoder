# 事故るのが嫌なのでU固定とする
# 理想は正方形なので、面積の和の平方根が１辺となることを目指してみる。

import random

def query(prdb):
    print(len(prdb))
    for p, r, d, b in prdb:
        print(p, r, d, b)
    W, H = map(int, input().split())
    return W, H

N, T, sigma = map(int, input().split())
wh = [tuple(map(int, input().split())) for _ in range(N)]

s_total = sum(map(lambda x: x[0]*x[1], wh))
sq = s_total**0.5

rng = random.Random(1234)

for _ in range(T):
    prdb = []

    i = 0
    while i < N:
        accum = 0
        while accum < sq and i < N:
            w, h = wh[i]
            r = rng.randint(0, 1)
            prdb.append((
                i,
                r,
                'U',
                -1 if accum == 0 else i-1,
            ))
            i += 1
            if r:
                w, h = h, w
            accum += w


    query(prdb)
