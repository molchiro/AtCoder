# 基本は縦長にする。長辺が今まで見たものよりも大きいなら横長に回転することで、凸凹が減るのではないかと考えた。
# これも微妙なので、回転でいい感じの貪欲を考えるのは捨てる

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
    border = random.randrange(int(sq*0.9), int(sq*1.1))
    while i < N:
        accum = 0
        top = max(wh[i])
        while accum < border and i < N:
            w, h = wh[i]
            r = 0
            # 一旦長編をhに持ってくる
            if w > h:
                w, h = h, w
                r = 1
            # 長辺が今までの高さより高いなら横にする
            if h > top:
                w, h = h, w
                r = (1+r)%2
            # 更新
            top = max(top, h)
            prdb.append((
                i,
                r,
                'U',
                -1 if accum == 0 else i-1,
            ))
            i += 1
            accum += w

    query(prdb)
