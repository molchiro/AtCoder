# A2から派生
# なんかうまくいかなかった？

import random

def query(prdb):
    print(len(prdb))
    for p, r, d, b in prdb:
        print(p, r, d, b)
    W, H = map(int, input().split())
    return W, H

N, T, sigma = map(int, input().split())
wh = [tuple(map(int, input().split())) for _ in range(N)]

# 正方形の箱に敷き詰めることができれば理論上の最適なので、理想の箱の1辺の長さを求める
s_total = sum(map(lambda x: x[0]*x[1], wh))
sq = s_total**0.5

rng = random.Random(1234)
rem = sum([max(w, h) for w, h in wh])

for _ in range(T):
    prdb = []

    i = 0

    # 実際に使う箱は理想値よりも若干大きくなるはずなので、上にぶれるように閾値をランダム生成
    border = random.randrange(int(sq), int(sq*1.1))

    while i < N:
        accum = 0
        while accum < border and i < N:
            w, h = wh[i]
            # 残り全部を横向きにしてもはみ出ないなら横向きにする（最後の行のはず）
            # それ以外はランダム
            # xxxxxxxxxxxxxxxxxxxうまくいっていないもよう
            if rem < border - accum:
                if w < h:
                    r = 1
                else:
                    r = 0
            else:
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
            rem -= w


    query(prdb)
