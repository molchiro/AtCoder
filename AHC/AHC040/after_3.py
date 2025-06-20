# 誤差修正パートでスキップ無しにする
# A9から派生

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

# 各列の高さの凸凹度と、箱の右辺の凸凹度を評価する
def eval(rows):
    score = 0
    row_box_list = []
    for row in rows:
        row_w = sum([w for w, h in row])
        row_h = max([h for w, h in row])
        row_box_list.append((row_w, row_h))
        score += sum([(row_h - h)*w for w, h in row])
    box_w = max([w for w, h in row_box_list])
    score += sum([(box_w -  w)*h  for w, h in row_box_list])
    return score

N, T, sigma = map(int, input().split())
wh = [list(map(int, input().split())) for _ in range(N)]

# 計測誤差の修正を試みる

for _ in range(N//4):
    u = []
    l = []
    prdb = []
    W = 0
    H = 0
    # vertに含まれる要素は縦方向に詰む
    vert = set(rng.sample(range(1, N), N//2))
    rot = []
    for i in range(N):
        w, h = wh[i]
        r = rng.randint(0, 1)
        rot.append(r)
        # １つめだけ必ず縦横両方に関与するので別処理
        if i == 0:
            u.append(i)
            l.append(i)

            prdb.append((i, r, 'U', -1))
            if r:
                H += w
                W += h
            else:
                H += h
                W += w
        else:
            if i in vert:
                u.append(i)
                prdb.append((i, r, 'U', -1))
                if r:
                    H += w
                else:
                    H += h
            else:
                l.append(i)
                prdb.append((i, r, 'L', -1))
                if r:
                    W += h
                else:
                    W += w

    W_, H_ = query(prdb)

    # 推測値と計測値の比率分修正する
    for idx in u:
        if rot[idx]:
            wh[idx][0] *= H_/H
        else:
            wh[idx][1] *= H_/H

    for idx in l:
        if rot[idx]:
            wh[idx][1] *= W_/W
        else:
            wh[idx][0] *= W_/W


# 本番開始
# 正方形の箱に敷き詰めることができれば理論上の最適なので、理想の箱の1辺の長さを求める
s_total = sum(map(lambda x: x[0]*x[1], wh))
ideal_edge_len = s_total**0.5

ct = 0
prdbs = []
score = []
seen = set()
# 時間オーバーか十分な試行回数が得られるまで繰り返す
while time.time() - start_time < 2.4 and ct < 10**6:
    prdb = []

    i = 0

    border = random.randrange(int(ideal_edge_len*0.98), int(ideal_edge_len*1.05))
    rows = [[]]
    while i < N:
        accum = 0
        while i < N:
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
            rows[-1].append((w, h))
        # 次の行用の配列を用意
        rows.append([])
    # 最後の配列は必ず空なので捨てる
    rows.pop()

    # 既出かどうか管理
    prdbstr = ''.join([str(r)+str(b) for p, r, d, b in prdb])
    if prdbstr in seen:
        continue
    seen.add(prdbstr)

    # 初見の操作は記録する
    prdbs.append(prdb)
    score.append((eval(rows), ct))
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