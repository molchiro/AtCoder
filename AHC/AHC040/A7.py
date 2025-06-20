# 評価関数について、一番大きい行と最後の行だけをみるようにしてみた

# A5から派生
import random
import time

# 開始時刻を記録
start_time = time.time()

def query(prdb):
    print(len(prdb))
    for p, r, b in prdb:
        print(p, r, 'U', b)
    W, H = map(int, input().split())
    return W, H

# max_w: 全ての行をにおいて最大のw　borderに近いほど良い
# last_w: 最後の行の幅 borderに近いほど良い
def eval(max_w, last_w, threshold):
    C_m = 1
    C_l = 1
    return abs(threshold-max_w)*C_m + abs(threshold-last_w)*C_l

N, T, sigma = map(int, input().split())
wh = [tuple(map(int, input().split())) for _ in range(N)]

# 正方形の箱に敷き詰めることができれば理論上の最適なので、理想の箱の1辺の長さを求める
s_total = sum(map(lambda x: x[0]*x[1], wh))
sq = s_total**0.5

rng = random.Random(1234)
rem = sum([max(w, h) for w, h in wh])

ct = 0
prdbs = []
score = []
seen = set()
# 時間オーバーか十分は試行回数が得られるまで繰り返す
while time.time() - start_time < 2.4 and ct < 2*10**5:
    prdb = []

    i = 0

    # 実際に使う箱は理想値よりも若干大きくなるはずなので、若干上にぶれるように閾値をランダム生成
    border = random.randrange(int(sq*0.98), int(sq*1.1))
    max_w = 0
    while i < N:
        accum = 0
        while accum < border and i < N:
            w, h = wh[i]
            r = rng.randint(0, 1)

            prdb.append((
                i,
                r,
                -1 if accum == 0 else i-1,
            ))
            i += 1
            if r:
                w, h = h, w
            accum += w
            rem -= w
        max_w = max(max_w, accum)

    prdbstr = ''.join([str(r)+str(b) for p, r, b in prdb])
    if prdbstr in seen:
        continue
    seen.add(prdbstr)
    prdbs.append(prdb)
    score.append((eval(max_w, accum, sq), ct))
    ct += 1

# print(prdbs[0])

# 上位スコアを出力する
score.sort()
# print(len(score), ct)
# print(score)
# print(prdbs[score[0][1]][0])
for i in range(T):
    s, idx = score[i]
    # print(s, idx)
    query(prdbs[idx])