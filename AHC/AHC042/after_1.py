from copy import deepcopy
import time
import random

start_time = time.time()
rng = random.Random(1234)

# 入力
N = int(input())

field = []

for i in range(N):
    C = list(input())
    field.append(C)

# 外周上の鬼　ただし角は複雑になるので無視する
edge_oni = []
for c in range(1, 19):
    if field[0][c] == 'x':
        edge_oni.append((0, c))
    if field[19][c] == 'x':
        edge_oni.append((19, c))
for r in range(1, 19):
    if field[r][0] == 'x':
        edge_oni.append((r, 0))
    if field[r][19] == 'x':
        edge_oni.append((r, 19))


# print(field)

def D(fld, i):
    res = 1 if fld[N-1][i] == 'x' else 0
    for h in range(N-1, 0, -1):
        fld[h][i] = fld[h-1][i]
    fld[0][i] = '.'
    return res

def U(fld, i):
    res = 1 if fld[0][i] == 'x' else 0
    for h in range(N-1):
        fld[h][i] = fld[h+1][i]
    fld[-1][i] = '.'
    return res

def R(fld, i):
    res = 1 if fld[i][N-1] == 'x' else 0
    for w in range(N-1, 0, -1):
        fld[i][w] = fld[i][w-1]
    fld[i][0] = '.'
    return res

def L(fld, i):
    res = 1 if fld[i][0] == 'x' else 0
    for w in range(N-1):
        fld[i][w] = fld[i][w+1]
    fld[i][-1] = '.'
    return res

SEARCH_ORDER = [11, 9, 13, 7, 15, 5, 17, 3, 19, 1, 10, 8, 12, 6, 14, 4, 16, 1, 18, 0] # 真ん中から初めて１つ飛ばしで探すとうまくあつまりそう

def solve():
    global field, edge_oni
    fld = deepcopy(field)
    res = []
    oni_remaining = 2*20

    # 外周の鬼をランダムに捨てて初期状態を乱数生成するパート
    # 捨てる順番をシャッフル
    shuffled_oni_order = edge_oni
    rng.shuffle(shuffled_oni_order)
    for r, c in shuffled_oni_order:
        if fld[r][c] != 'x':
            continue
        
        # 捨てるかどうか確率で決める
        if rng.random() > 0.5:
            if r == 0:
                res.append(('U', c))
                oni_remaining -= U(fld, c)
            elif r == 19:
                res.append(('D', c))
                oni_remaining -= D(fld, c)
            elif c == 0:
                res.append(('L', r))
                oni_remaining -= L(fld, r)
            else:
                res.append(('R', r))
                oni_remaining -= R(fld, r)
    
    for i in range(2*40):
        if oni_remaining <= 0:
            break

        # 鬼だけになったか交互になっていない行or列を処理

        # 行方向に探索
        for r in SEARCH_ORDER:
            oni_min = 20
            oni_max = -1
            oni_n = 0
            huku_min = 20
            huku_max = -1
            huku_f = 0
            for c in range(N):
                if fld[r][c] == 'x':
                    oni_n += 1
                    oni_min = min(oni_min, c)
                    oni_max = max(oni_max, c)
                elif fld[r][c] == 'o':
                    huku_f = 1
                    huku_min = min(huku_min, c)
                    huku_max = max(huku_max, c)

            # 鬼がいない時は何もしない
            if not oni_n:
                continue

            if huku_f:
                if oni_max < huku_min:
                    # 福より左にしか鬼がいない

                    # 鬼の密度が低ければスキップ
                    if oni_n/(oni_max+1) < 0.5/(i+1):
                        continue

                    for _ in range(oni_max+1):
                        # 操作しようとしている列の上下を巻き込めそうなら巻き込む
                        for c in range(min(oni_max+2, 20)):
                            if r < N-1 and fld[r][c] != 'x' and fld[r+1][c] == 'x' and fld[0][c] != 'o':
                                res.append(('U', c))
                                oni_remaining -= U(fld, c)
                            elif r > 0 and fld[r][c] != 'x' and fld[r-1][c] == 'x' and fld[-1][c] != 'o':
                                res.append(('D', c))
                                oni_remaining -= D(fld, c)
                        
                        res.append(('L', r))
                        oni_remaining -= L(fld, r)
                elif huku_max < oni_min:
                    # 福より右にしか鬼がいない

                    # 鬼の密度が低ければスキップ
                    if oni_n/(N-oni_min) < 0.5/(i+1):
                        continue

                    for _ in range(N-oni_min):
                        # 操作しようとしている列の上下を巻き込めそうなら巻き込む
                        for c in range(N-1, max(oni_min-2, -1), -1):
                            if r < N-1 and fld[r][c] != 'x' and fld[r+1][c] == 'x' and fld[0][c] != 'o':
                                res.append(('U', c))
                                oni_remaining -= U(fld, c)
                            elif r > 0 and fld[r][c] != 'x' and fld[r-1][c] == 'x' and fld[-1][c] != 'o':
                                res.append(('D', c))
                                oni_remaining -= D(fld, c)
                        res.append(('R', r))
                        oni_remaining -= R(fld, r)
                    
            else:
                # 鬼しかいないなら端に近い方の方向に全部なくなるまで動かす
                if oni_min < N-1 - oni_max:

                    # 鬼の密度が低ければスキップ
                    if oni_n/(oni_max+1) < 0.5/(i+1):
                        continue


                    for _ in range(oni_max+1):
                        # 操作しようとしている列の上下を巻き込めそうなら巻き込む
                        for c in range(min(oni_max+2, 20)):
                            if r < N-1 and fld[r][c] != 'x' and fld[r+1][c] == 'x' and fld[0][c] != 'o':
                                res.append(('U', c))
                                oni_remaining -= U(fld, c)
                            elif r > 0 and fld[r][c] != 'x' and fld[r-1][c] == 'x' and fld[-1][c] != 'o':
                                res.append(('D', c))
                                oni_remaining -= D(fld, c)
                        res.append(('L', r))
                        oni_remaining -= L(fld, r)
                else:

                    # 鬼の密度が低ければスキップ
                    if oni_n/(N-oni_min) < 0.5/(i+1):
                        continue

                    for _ in range(N-oni_min):
                        # 操作しようとしている列の上下を巻き込めそうなら巻き込む
                        for c in range(N-1, min(oni_min-2, -1), -1):
                            if r < N-1 and fld[r][c] != 'x' and fld[r+1][c] == 'x' and fld[0][c] != 'o':
                                res.append(('U', c))
                                oni_remaining -= U(fld, c)
                            elif r > 0 and fld[r][c] != 'x' and fld[r-1][c] == 'x' and fld[-1][c] != 'o':
                                res.append(('D', c))
                                oni_remaining -= D(fld, c)
                        res.append(('R', r))
                        oni_remaining -= R(fld, r)
                    
        
        # 列方向に探索
        for c in SEARCH_ORDER:

            oni_min = 20
            oni_max = -1
            oni_n = 0
            huku_min = 20
            huku_max = -1
            huku_f = 0
            for r in range(N):
                if fld[r][c] == 'x':
                    oni_n += 1
                    oni_min = min(oni_min, r)
                    oni_max = max(oni_max, r)
                elif fld[r][c] == 'o':
                    huku_f = 1
                    huku_min = min(huku_min, r)
                    huku_max = max(huku_max, r)

            # 鬼がいない時は何もしない
            if not oni_n:
                continue

            if huku_f:
                if oni_max < huku_min:
                    # 福より上にしか鬼がいない

                    # 鬼の密度が低ければスキップ
                    if oni_n/(oni_max+1) < 0.5/(i+1):
                        continue

                    for _ in range(oni_max+1):
                        # 左右を巻き込む
                        for r in range(min(oni_max+2, 20)):
                            if c < N-1 and fld[r][c] != 'x' and fld[r][c+1] == 'x' and fld[r][0] != 'o':
                                res.append(('L', r))
                                oni_remaining -= L(fld, r)
                            elif c > 0 and fld[r][c] != 'x' and fld[r][c-1] == 'x' and fld[r][-1] != 'o':
                                res.append(('R', r))
                                oni_remaining -= R(fld, r)
                        res.append(('U', c))
                        oni_remaining -= U(fld, c)
                    diff_f = 1
                    
                elif huku_max < oni_min:
                    # 福より下にしか鬼がいない

                    # 鬼の密度が低ければスキップ
                    if oni_n/(N-oni_min) < 0.5/(i+1):
                        continue


                    for _ in range(N-oni_min):
                        # 左右を巻き込む
                        for r in range(N-1, max(oni_min-2, -1), -1):
                            if c < N-1 and fld[r][c] != 'x' and fld[r][c+1] == 'x' and fld[r][0] != 'o':
                                res.append(('L', r))
                                oni_remaining -= L(fld, r)
                            elif c > 0 and fld[r][c] != 'x' and fld[r][c-1] == 'x' and fld[r][-1] != 'o':
                                res.append(('R', r))
                                oni_remaining -= R(fld, r)
                        res.append(('D', c))
                        oni_remaining -= D(fld, c)
                    
            else:
                # 鬼しかいないなら端に近い方の方向に全部なくなるまで動かす
                if oni_min < N-1 - oni_max:

                    # 鬼の密度が低ければスキップ
                    if oni_n/(oni_max+1) < 0.5/(i+1):
                        continue

                    for _ in range(oni_max+1):
                        # 左右を巻き込む
                        for r in range(min(oni_max+1, 20)):
                            if c < N-1 and fld[r][c] != 'x' and fld[r][c+1] == 'x' and fld[r][0] != 'o':
                                res.append(('L', r))
                                oni_remaining -= L(fld, r)
                            elif c > 0 and fld[r][c] != 'x' and fld[r][c-1] == 'x' and fld[r][-1] != 'o':
                                res.append(('R', r))
                                oni_remaining -= R(fld, r)
                        res.append(('U', c))
                        oni_remaining -= U(fld, c)
                else:

                    # 鬼の密度が低ければスキップ
                    if oni_n/(N-oni_min) < 0.5/(i+1):
                        continue

                    for _ in range(N-oni_min):
                        # 左右を巻き込む
                        for r in range(N-1, oni_min, -1):
                            if c < N-1 and fld[r][c] != 'x' and fld[r][c+1] == 'x' and fld[r][0] != 'o':
                                res.append(('L', r))
                                oni_remaining -= L(fld, r)
                            elif c > 0 and fld[r][c] != 'x' and fld[r][c-1] == 'x' and fld[r][-1] != 'o':
                                res.append(('R', r))
                                oni_remaining -= R(fld, r)
                        res.append(('D', c))
                        oni_remaining -= D(fld, c)

    if oni_remaining > 0:
        score = 4*20*20-20*(oni_remaining)
    else:
        score = 8*20*20-len(res)
    return res[:], score

ans = []
score = 800

while time.time() - start_time < 1.8:
    new_ans, new_score = solve()
    if new_score > score:
        ans = new_ans

for i in range(min(len(ans), 4*N*N)):
    print(*ans[i])