import sys
sys.setrecursionlimit(10**9)

N = int(input())
P = list(map(int, input().split()))

from atcoder.segtree import SegTree

seg = SegTree(lambda x, y: max(x, y), 0, P)
d = { v: i for i, v in enumerate(P)}

from functools import cache

# 左側に行かせるのと右側に行かせるのどっちが良いか
@cache
def solve(l, r): # 今つながっている範囲を(l, r)
    global N, P
    if l == r:
        return 0

    # 今いる場所
    M = seg.prod(l, r+1)
    now = d[M]
    # print(l, r, M, now)
    if now == l:
        # 必ず右に行く場合
        M_to = seg.prod(l+1, r+1)
        to = d[M_to]
        return abs(to-now) + solve(l+1, r)
    elif now == r:
        # 必ず左に行く場合
        M_to = seg.prod(l, r)
        to = d[M_to]
        return abs(to-now) + solve(l, r-1)
    else:
        M_left = seg.prod(l, now)
        M_right = seg.prod(now+1, r+1)

        # 左に行った場合の運動量
        to_left = d[M_left]
        cost_left = abs(now-to_left) + solve(l, now-1)
        
        to_right = d[M_right]
        cost_right = abs(to_right-now) + solve(now+1, r)

        return max(cost_left, cost_right)

print(solve(0, N-1))