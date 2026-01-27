from functools import cmp_to_key

# 全周バージョン [0..2π)
def cmp_arg_ccw_from_posx(a, b):
    ax, ay = a
    bx, by = b

    # x軸を含んで上側とそれ以外をまず判定
    ha = 0 if (ay > 0 or (ay == 0 and ax >= 0)) else 1
    hb = 0 if (by > 0 or (by == 0 and bx >= 0)) else 1
    if ha != hb:
        return ha - hb

    # 同じ側にいるなら外積で比較
    return ay * bx - ax * by

# --- tests / asserts ---
p = [(0, 1), (1, -2), (-2, 0)]
assert sorted(p, key=cmp_to_key(cmp_arg_ccw_from_posx)) == [(0, 1), (-2, 0), (1, -2)]

p2 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
assert sorted(p2, key=cmp_to_key(cmp_arg_ccw_from_posx)) == [(1, 0), (0, 1), (-1, 0), (0, -1)]

p3 = [(2, 2), (1, 1), (3, 3), (1, 0)]
assert sorted(p3, key=cmp_to_key(cmp_arg_ccw_from_posx)) == [(1, 0), (2, 2), (1, 1), (3, 3)]


# 傾きのみバージョン (-π/2, -π/2]
from functools import cmp_to_key

def cmp_slope_minus90_to_90(a, b):
    ax, ay = a
    bx, by = b

    return ay * bx - ax * by

# --- asserts ---
p2 = [(1, -2), (2, -1), (1, 0), (2, 1), (1, 2), (0, 5)]
assert sorted(p2, key=cmp_to_key(cmp_slope_minus90_to_90)) == [
    (1, -2),
    (2, -1),
    (1, 0),
    (2, 1),
    (1, 2),
    (0, 5),
]

p3 = [(1, 1), (-1, -1), (2, 2)]
assert sorted(p3, key=cmp_to_key(cmp_slope_minus90_to_90)) == [(1, 1), (-1, -1), (2, 2)]

print("all asserts passed")
