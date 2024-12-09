from functools import cache
import sys

sys.setrecursionlimit(10**9)

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]

from atcoder.segtree import SegTree

l_sg = SegTree(max, 0, [x[0] for x in lines])
u_sg = SegTree(min, 10**10, [x[1] for x in lines])

@cache
def through_range(u, v):
    if u > v:
        u, v = v, u
    global l_sg, u_sg
    return l_sg.prod(u, v+1), u_sg.prod(u, v+1)

@cache
def through_to_right(x, y):
    global N
    ok = x
    ng = N
    while ng - ok > 1:
        test = (ng+ok)//2
        l, u = through_range(x, test)
        if l <= y <= u:
            ok = test
        else:
            ng = test
    return ok

@cache
def move_right(sx, sy, tx):
    global lines
    # print('solve', sx, sy)
    # 同じ列にいたら終了
    if sx == tx:
        return 0, sy
    
    # 隣の列に最短で移動
    next_line = lines[sx+1]
    L, U = next_line
    next_sy = min(max(sy, L), U)
    cost, y = move_right(sx+1, next_sy, tx)
    return 1 + abs(next_sy - sy) + cost, y

Q = int(input())
for _ in range(Q):
    sx, sy, tx, ty = list(map(int, input().split()))
    sx -= 1
    tx -= 1
    # キャッシュ削減のため、sx <= txに直す
    if sx > tx:
        # print('swap')
        sx, sy, tx, ty = tx, ty, sx, sy

    ans = 0
    # sからyを変えずに行けるところまで右に行く
    sx_through = min(through_to_right(sx, sy), tx)
    ans += sx_through - sx
    sx = sx_through
    # tからyを変えずに行けるところまで左に行く
    # tlx = through_to_left(tx, ty)
    # ans += tx - max(sx, tlx)
    # tx = max(sx, tlx)
    # 右に移動
    cost, y = move_right(sx, sy, tx)
    ans += cost
    # 縦移動
    ans += abs(y - ty)
    print(ans)

        