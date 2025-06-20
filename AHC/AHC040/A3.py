# 回転をいい感じに工夫してみたい。長辺が横か縦かを揃えてみたら、行の縦方向の凸凹がうまく馴染まないか
# => あまり効果なし

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
    f = 0
    border = random.randrange(int(sq*0.9), int(sq*1.1))
    while i < N:
        accum = 0
        f = (f+1)%2
        while accum < border and i < N:
            w, h = wh[i]
            r = 0
            # 行ごとに縦横交互に並べる
            if (w < h) == f:
                w, h = h, w
                r = 1
            prdb.append((
                i,
                r,
                'U',
                -1 if accum == 0 else i-1,
            ))
            i += 1
            accum += w

    query(prdb)
