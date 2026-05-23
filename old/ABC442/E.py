N, Q = list(map(int, input().split()))
monsters = []
for i in range(N):
    X, Y = list(map(int, input().split()))
    monsters.append((X, Y, i))

from functools import cmp_to_key

# 全周バージョン [0..2π)
def cmp_arg_ccw_from_posx(a, b):
    ax, ay, _ = a
    bx, by, _ = b

    # x軸を含んで上側とそれ以外をまず判定
    ha = 0 if (ay > 0 or (ay == 0 and ax >= 0)) else 1
    hb = 0 if (by > 0 or (by == 0 and bx >= 0)) else 1
    if ha != hb:
        return ha - hb

    # 同じ側にいるなら外積で比較
    return ay * bx - ax * by

monsters.sort(key = cmp_to_key(cmp_arg_ccw_from_posx), reverse=True)

# 同じ傾きのモンスターを圧縮
monsters_compressed_p = []
monsters_compressed_l = []
first = monsters[0]
monsters_compressed_p.append((first[0], first[1]))
monsters_compressed_l.append([first[2]])
for i in range(1, N):
    x_prev, y_prev = monsters_compressed_p[-1]
    x_i, y_i, idx = monsters[i]
    if cmp_arg_ccw_from_posx((x_prev, y_prev, None), (x_i, y_i, None)) == 0:
        monsters_compressed_l[-1].append(idx)
    else:
        monsters_compressed_p.append((x_i, y_i))
        monsters_compressed_l.append([idx])
N_compressed = len(monsters_compressed_p)

# 圧縮配列の何番目にいるか記録
monster_index = {}
for i, l in enumerate(monsters_compressed_l):
    for idx in l:
        monster_index[idx] = i

# print(monsters_compressed_p)
# print(monsters_compressed_l)
# print(monster_index)

# 累積和を2周分用意
cumsum = [0]
for l in monsters_compressed_l:
   cumsum.append(cumsum[-1] + len(l))
for l in monsters_compressed_l:
   cumsum.append(cumsum[-1] + len(l))
# print(cumsum)


for _ in range(Q):
    A, B = list(map(lambda x: int(x) - 1, input().split()))
    l = monster_index[A]
    r = monster_index[B]
    if l > r:
       r += N_compressed
    print(cumsum[r+1]-cumsum[l])

