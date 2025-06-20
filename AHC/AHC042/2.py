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
        for r in range(N):
            oni_min = 20
            oni_max = -1
            oni_f = 0
            huku_min = 20
            huku_max = -1
            huku_f = 0
            for c in range(N):
                if fld[r][c] == 'x':
                    oni_f = 1
                    oni_min = min(oni_min, c)
                    oni_max = max(oni_max, c)
                elif fld[r][c] == 'o':
                    huku_f = 1
                    huku_min = min(huku_min, c)
                    huku_max = max(huku_max, c)

            # 鬼がいない時は何もしない
            if not oni_f:
                continue

            if huku_f:
                if oni_max < huku_min:
                    # 福より左にしか鬼がいない
                    for _ in range(oni_max+1):
                        res.append(('L', r))
                        oni_remaining -= L(fld, r)
                    diff_f = 1
                elif huku_max < oni_min:
                    # 福より右にしか鬼がいない
                    for _ in range(N-oni_min):
                        res.append(('R', r))
                        oni_remaining -= R(fld, r)
                    diff_f = 1
            else:
                diff_f = 1
                # 鬼しかいないなら端に近い方の方向に全部なくなるまで動かす
                if oni_min < N-1 - oni_max:
                    for _ in range(oni_max+1):
                        res.append(('L', r))
                        oni_remaining -= L(fld, r)
                else:
                    for _ in range(N-oni_min):
                        res.append(('R', r))
                        oni_remaining -= R(fld, r)
        
        # 列方向に探索
        for c in range(N):
            oni_min = 20
            oni_max = -1
            oni_f = 0
            huku_min = 20
            huku_max = -1
            huku_f = 0
            for r in range(N):
                if fld[r][c] == 'x':
                    oni_f = 1
                    oni_min = min(oni_min, r)
                    oni_max = max(oni_max, r)
                elif fld[r][c] == 'o':
                    huku_f = 1
                    huku_min = min(huku_min, r)
                    huku_max = max(huku_max, r)

            # 鬼がいない時は何もしない
            if not oni_f:
                continue

            if huku_f:
                if oni_max < huku_min:
                    # 福より上にしか鬼がいない
                    for _ in range(oni_max+1):
                        res.append(('U', c))
                        oni_remaining -= U(fld, c)
                    diff_f = 1
                    
                elif huku_max < oni_min:
                    # 福より下にしか鬼がいない
                    for _ in range(N-oni_min):
                        res.append(('D', c))
                        oni_remaining -= D(fld, c)
                    diff_f = 1
                    
            else:
                # 鬼しかいないなら端に近い方の方向に全部なくなるまで動かす
                diff_f = 1

                if oni_min < N-1 - oni_max:
                    for _ in range(oni_max+1):
                        res.append(('U', c))
                        oni_remaining -= U(fld, c)
                else:
                    for _ in range(N-oni_min):
                        res.append(('D', c))
                        oni_remaining -= D(fld, c)

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
    if oni_c < min(oni_r, N-1 - oni_r):
        # 左に寄っている時
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
            # どっちにも動かせない時は詰み
            break

    else:
    # elif N-1 - oni_c < min(oni_r, N-1 - oni_r):
        # 右に寄っている時
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
            # どっちにも動かせない時は詰み
            break


    if new_oni < oni:
        oni = new_oni
        tentative_ans += more_ans
        more_ans = []

ans = tentative_ans + more_ans

for i in range(min(len(ans), 4*N*N)):
    print(*ans[i])