# 誤差修正を試みる

# A5から派生
import random
import time

rng = random.Random(1234)

# 開始時刻を記録
start_time = time.time()

def query(prdb):
    print(len(prdb))
    for p, r,d, b in prdb:
        print(p, r, d, b)
    W, H = map(int, input().split())
    return W, H

# デコボコ具合と正方形度を評価
def eval(rows, sq):
    C_1 = 1
    C_2 = 0
    max_w = max(rows)
    return sum([(max_w-w) for w in rows])*C_1 + abs(max_w-sq)*sq*C_2

N, T, sigma = map(int, input().split())
wh = [list(map(int, input().split())) for _ in range(N)]

# 計測誤差の修正を試みる

for _ in range(N//4):
    u = []
    l = []
    prdb = []
    W = 0
    H = 0
    for i in range(N):
        w, h = wh[i]
        rand = rng.random()
        # 15%の確率で縦に、もう15％の確率で横に積み上げる
        if rand > .3:
            continue
        if len(u) == 0:
            u.append(i)
            l.append(i)
            prdb.append((i, 0, 'U', -1))
            W += w
            H += h
        elif rand < .15:
            u.append(i)
            prdb.append((i, 0, 'U', -1))
            H += h
        else:
            l.append(i)
            prdb.append((i, 0, 'L', -1))
            W += w
        
    # １つも選ばれていなければ１つ選ぶ
    if len(u) == 0:
        x = int(N*rng.random())
        u.append(x)
        l.append(x)
        prdb.append((x, 0, 'U', -1))
        W += w
        H += h
    
    W_, H_ = query(prdb)

    # 推測値と計測値の比率分修正する
    for idx in u:
        wh[idx][1] *= H_/H
    for idx in l:
        wh[idx][0] *= W_/W


# 本番開始
# 正方形の箱に敷き詰めることができれば理論上の最適なので、理想の箱の1辺の長さを求める
s_total = sum(map(lambda x: x[0]*x[1], wh))
sq = s_total**0.5

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
    rows = []
    while i < N:
        accum = 0
        while accum < border and i < N:
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
            rem -= w
        rows.append(accum)

    prdbstr = ''.join([str(r)+str(b) for p, r, d, b in prdb])
    if prdbstr in seen:
        continue
    seen.add(prdbstr)
    prdbs.append(prdb)
    score.append((eval(rows, sq), ct))
    ct += 1

# print(prdbs[0])

# 上位スコアを出力する
score.sort()
# print(len(score), ct)
# print(score)
# print(prdbs[score[0][1]][0])
for i in range(T-N//4):
    s, idx = score[i]
    # print(s, idx)
    query(prdbs[idx])