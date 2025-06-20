# 行or列で一気に捨てる時に近くのやつも道連れにするパターン
# さらに鬼だけの時も効率を重視してみる

from copy import deepcopy

# 入力
N = int(input())

field = []

for i in range(N):
    C = list(input())
    field.append(C)

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

THRESHOLD = 9

def solve(fld, oni_remaining):
    fld = deepcopy(fld)
    res = []

    # 貪欲前処理パート
    # 外周を捨てる
    # 上辺
    for c in range(N):
        while fld[0][c] == 'x':
            res.append(('U', c))
            oni_remaining -= U(fld, c)
    # 右辺
    for r in range(N):
        while fld[r][-1] == 'x':
            res.append(('R', r))
            oni_remaining -= R(fld, r)
    # 下辺
    for c in range(N):
        while fld[-1][c] == 'x':
            res.append(('D', c))
            oni_remaining -= D(fld, c)
    # 左辺
    for r in range(N):
        while fld[r][0] == 'x':
            res.append(('L', r))
            oni_remaining -= L(fld, r)

    # 鬼だけになったか交互になっていない行or列を処理
    # 状況が変わらなくなるまで繰り返す
    diff_f = 1
    while diff_f:
        diff_f = 0
        # 行方向に探索
        skip = 0
        for r in range(N):
            if skip:
                skip = 0
                continue
            
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

                    # 鬼が一人の時は効率が悪ければスキップ
                    if oni_n == 1 and oni_max > THRESHOLD:
                        continue

                    # 操作しようとしている列の上下を巻き込めそうなら巻き込む
                    for c in range(oni_max):
                        if r < N-1 and fld[r][c] != 'x' and fld[r+1][c] == 'x' and fld[0][c] != 'o':
                            res.append(('U', c))
                            oni_remaining -= U(fld, c)
                        elif r > 0 and fld[r][c] != 'x' and fld[r-1][c] == 'x' and fld[-1][c] != 'o':
                            res.append(('D', c))
                            oni_remaining -= D(fld, c)
                        
                    for _ in range(oni_max+1):
                        res.append(('L', r))
                        oni_remaining -= L(fld, r)
                    skip = 1
                    diff_f = 1
                elif huku_max < oni_min:
                    # 福より右にしか鬼がいない

                    # 鬼が一人の時は効率が悪ければスキップ
                    if oni_n == 1 and N-oni_min > THRESHOLD:
                        continue

                    # 操作しようとしている列の上下を巻き込めそうなら巻き込む
                    for c in range(N-1, oni_min, -1):
                        if r < N-1 and fld[r][c] != 'x' and fld[r+1][c] == 'x' and fld[0][c] != 'o':
                            res.append(('U', c))
                            oni_remaining -= U(fld, c)
                        elif r > 0 and fld[r][c] != 'x' and fld[r-1][c] == 'x' and fld[-1][c] != 'o':
                            res.append(('D', c))
                            oni_remaining -= D(fld, c)
                    for _ in range(N-oni_min):
                        res.append(('R', r))
                        oni_remaining -= R(fld, r)
                    skip = 1
                    
                    diff_f = 1
            else:
                # 鬼しかいないなら端に近い方の方向に全部なくなるまで動かす
                if oni_min < N-1 - oni_max:
                    # 鬼が一人の時は効率が悪ければスキップ
                    if oni_n == 1 and oni_max > THRESHOLD:
                        continue

                    # 操作しようとしている列の上下を巻き込めそうなら巻き込む
                    for c in range(oni_max):
                        if r < N-1 and fld[r][c] != 'x' and fld[r+1][c] == 'x' and fld[0][c] != 'o':
                            res.append(('U', c))
                            oni_remaining -= U(fld, c)
                        elif r > 0 and fld[r][c] != 'x' and fld[r-1][c] == 'x' and fld[-1][c] != 'o':
                            res.append(('D', c))
                            oni_remaining -= D(fld, c)
                    for _ in range(oni_max+1):
                        res.append(('L', r))
                        oni_remaining -= L(fld, r)
                    diff_f = 1
                    skip = 1
                else:
                    # 鬼が一人の時は効率が悪ければスキップ
                    if oni_n == 1 and N-oni_min > THRESHOLD:
                        continue

                    # 操作しようとしている列の上下を巻き込めそうなら巻き込む
                    for c in range(N-1, oni_min, -1):
                        if r < N-1 and fld[r][c] != 'x' and fld[r+1][c] == 'x' and fld[0][c] != 'o':
                            res.append(('U', c))
                            oni_remaining -= U(fld, c)
                        elif r > 0 and fld[r][c] != 'x' and fld[r-1][c] == 'x' and fld[-1][c] != 'o':
                            res.append(('D', c))
                            oni_remaining -= D(fld, c)

                    for _ in range(N-oni_min):
                        res.append(('R', r))
                        oni_remaining -= R(fld, r)
                    
                    diff_f = 1
                    skip = 1
        
        # 列方向に探索
        skip = 0
        for c in range(N):
            if skip:
                skip = 0
                continue

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

                    # 鬼が一人の時は効率が悪ければスキップ
                    if oni_n == 1 and oni_max > THRESHOLD:
                        continue

                    # 左右を巻き込む
                    for r in range(oni_max):
                        if c < N-1 and fld[r][c] != 'x' and fld[r][c+1] == 'x' and fld[r][0] != 'o':
                            res.append(('L', r))
                            oni_remaining -= L(fld, r)
                        elif c > 0 and fld[r][c] != 'x' and fld[r][c-1] == 'x' and fld[r][-1] != 'o':
                            res.append(('R', r))
                            oni_remaining -= R(fld, r)
                    for _ in range(oni_max+1):
                        res.append(('U', c))
                        oni_remaining -= U(fld, c)
                    diff_f = 1
                    skip = 1
                    
                elif huku_max < oni_min:
                    # 福より下にしか鬼がいない

                    # 鬼が一人の時は効率が悪ければスキップ
                    if oni_n == 1 and N-oni_min > THRESHOLD:
                        continue

                    # 左右を巻き込む
                    for r in range(N-1, oni_min, -1):
                        if c < N-1 and fld[r][c] != 'x' and fld[r][c+1] == 'x' and fld[r][0] != 'o':
                            res.append(('L', r))
                            oni_remaining -= L(fld, r)
                        elif c > 0 and fld[r][c] != 'x' and fld[r][c-1] == 'x' and fld[r][-1] != 'o':
                            res.append(('R', r))
                            oni_remaining -= R(fld, r)
                    for _ in range(N-oni_min):
                        res.append(('D', c))
                        oni_remaining -= D(fld, c)
                    diff_f = 1
                    skip = 1

                    
            else:
                # 鬼しかいないなら端に近い方の方向に全部なくなるまで動かす
                if oni_min < N-1 - oni_max:

                    # 鬼が一人の時は効率が悪ければスキップ
                    if oni_n == 1 and oni_max > THRESHOLD:
                        continue

                    # 左右を巻き込む
                    for r in range(oni_max):
                        if c < N-1 and fld[r][c] != 'x' and fld[r][c+1] == 'x' and fld[r][0] != 'o':
                            res.append(('L', r))
                            oni_remaining -= L(fld, r)
                        elif c > 0 and fld[r][c] != 'x' and fld[r][c-1] == 'x' and fld[r][-1] != 'o':
                            res.append(('R', r))
                            oni_remaining -= R(fld, r)
                    for _ in range(oni_max+1):
                        res.append(('U', c))
                        oni_remaining -= U(fld, c)
                    diff_f = 1
                    skip = 1

                else:

                    # 鬼が一人の時は効率が悪ければスキップ
                    if oni_n == 1 and N-oni_min > THRESHOLD:
                        continue

                    # 左右を巻き込む
                    for r in range(N-1, oni_min, -1):
                        if c < N-1 and fld[r][c] != 'x' and fld[r][c+1] == 'x' and fld[r][0] != 'o':
                            res.append(('L', r))
                            oni_remaining -= L(fld, r)
                        elif c > 0 and fld[r][c] != 'x' and fld[r][c-1] == 'x' and fld[r][-1] != 'o':
                            res.append(('R', r))
                            oni_remaining -= R(fld, r)
                    for _ in range(N-oni_min):
                        res.append(('D', c))
                        oni_remaining -= D(fld, c)

                    diff_f = 1
                    skip = 1

    return oni_remaining, res[:], fld

oni, tentative_ans, field = solve(field, 2*N)

# print(oni)

# 試行錯誤パート
# 鬼のいる場所について、上下左右に適当に動かしてみてもう一度解く
more_ans = []
while oni:
    # 鬼を探索
    for r in range(N):
        for c in range(N):
            if field[r][c] == 'x':
                break
        if field[r][c] == 'x':
                break
        
    oni_r = r
    oni_c = c
    # print(oni_r, oni_c)

    # 上下方向と左右方向のどちらに動かすべきか判定
    if min(oni_c, N-1 - oni_c) < min(oni_r, N-1 - oni_r):
        # 左右どちらかに寄っている時は上下を試す
        if field[0][oni_c] != 'o':
            # 上に動かせるとき、上に動かして解いてみる
            # 直前の操作が同じ列を下に動かす操作だったなら千日手なので諦める
            # [memo]: 左右の操作を試すと改善できるかも？
            if more_ans and more_ans[-1] == ('D', oni_c):
                break

            more_ans.append(('U', oni_c))
            U(field, oni_c)
            new_oni, actions, field = solve(field, oni)
            more_ans += actions

        elif field[-1][oni_c] != 'o':
            # 下に動かせるとき、下に動かして解いてみる
            # 直前の操作が同じ列を上に動かす操作だったなら千日手なので諦める
            # [memo]: 左右の操作を試すと改善できるかも？
            if more_ans and more_ans[-1] == ('U', oni_c):
                break

            more_ans.append(('D', oni_c))
            D(field, oni_c)
            new_oni, actions, field = solve(field, oni)
            more_ans += actions
        else:
            # どっちもだめなら左右を試す
            if field[oni_r][0] != 'o':
                # 左に動かせるとき、左に動かして解いてみる
                # 直前の操作が同じ列を右に動かす操作だったなら千日手なので諦める
                # [memo]: 上下の操作を試すと改善できるかも？
                if more_ans and more_ans[-1] == ('R', oni_r):
                    break

                more_ans.append(('L', oni_r))
                L(field, oni_r)
                new_oni, actions, field = solve(field, oni)
                more_ans += actions
            elif field[oni_r][-1] != 'o':
                # 右に動かせるとき、右に動かして解いてみる
                # 直前の操作が同じ列を上に動かす操作だったなら千日手なので諦める
                # [memo]: 上下の操作を試すと改善できるかも？
                if more_ans and more_ans[-1] == ('L', oni_r):
                    break

                more_ans.append(('R', oni_r))
                R(field, oni_r)
                new_oni, actions, field = solve(field, oni)
                more_ans += actions
            else:
                # それでもダメなら詰み
                break

    else:
        # 上下どちらかに寄っている時は左右を試す
        if field[oni_r][0] != 'o':
            # 左に動かせるとき、左に動かして解いてみる
            # 直前の操作が同じ列を右に動かす操作だったなら千日手なので諦める
            # [memo]: 上下の操作を試すと改善できるかも？
            if more_ans and more_ans[-1] == ('R', oni_r):
                break

            more_ans.append(('L', oni_r))
            L(field, oni_r)
            new_oni, actions, field = solve(field, oni)
            more_ans += actions
        elif field[oni_r][-1] != 'o':
            # 右に動かせるとき、右に動かして解いてみる
            # 直前の操作が同じ列を上に動かす操作だったなら千日手なので諦める
            # [memo]: 上下の操作を試すと改善できるかも？
            if more_ans and more_ans[-1] == ('L', oni_r):
                break

            more_ans.append(('R', oni_r))
            R(field, oni_r)
            new_oni, actions, field = solve(field, oni)
            more_ans += actions
        else:
            # 左右に動かせないなら上下を試す
            if field[0][oni_c] != 'o':
                # 上に動かせるとき、上に動かして解いてみる
                # 直前の操作が同じ列を下に動かす操作だったなら千日手なので諦める
                # [memo]: 左右の操作を試すと改善できるかも？
                if more_ans and more_ans[-1] == ('D', oni_c):
                    break

                more_ans.append(('U', oni_c))
                U(field, oni_c)
                new_oni, actions, field = solve(field, oni)
                more_ans += actions

            elif field[-1][oni_c] != 'o':
                # 下に動かせるとき、下に動かして解いてみる
                # 直前の操作が同じ列を上に動かす操作だったなら千日手なので諦める
                # [memo]: 左右の操作を試すと改善できるかも？
                if more_ans and more_ans[-1] == ('U', oni_c):
                    break

                more_ans.append(('D', oni_c))
                D(field, oni_c)
                new_oni, actions, field = solve(field, oni)
                more_ans += actions
            else:
                # それでもダメなら詰み
                break

    if new_oni < oni:
        oni = new_oni
        tentative_ans += more_ans
        more_ans = []

ans = tentative_ans + more_ans

for i in range(min(len(ans), 4*N*N)):
    print(*ans[i])