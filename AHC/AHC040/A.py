# 5%のグッズを箱に入れないことにしてみる => 悪化した。よく考えたら当たり前だった。

import random

def query(prdb):
    print(len(prdb))
    for p, r, d, b in prdb:
        print(p, r, d, b)
    W, H = map(int, input().split())
    return W, H

N, T, sigma = map(int, input().split())
wh = [tuple(map(int, input().split())) for _ in range(N)]

rng = random.Random(1234)

drop = 0.05

for _ in range(T):
    choiced = [-1]
    prdb = []
    for i in range(N):

        prdb.append((
            i,
            rng.randint(0, 1),
            ['U', 'L'][rng.randint(0, 1)],
            rng.choice(choiced),
        ))
        choiced.append(i)
    query(prdb)
