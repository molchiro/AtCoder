N, Q = list(map(int, input().split()))
trees = [list(map(int, input().split())) for _ in range(N)]
rotated_trees = [(x+y, x-y) for x, y in trees]

from atcoder.segtree import SegTree

w_min_seg = SegTree(lambda x, y:min(x, y), 10**18, [w for w, _ in rotated_trees])
w_max_seg = SegTree(lambda x, y:max(x, y), -10**18, [w for w, _ in rotated_trees])
v_min_seg = SegTree(lambda x, y:min(x, y), 10**18, [v for _, v in rotated_trees])
v_max_seg = SegTree(lambda x, y:max(x, y), -10**18, [v for _, v in rotated_trees])

for _ in range(Q):
    t, *params = list(map(int, input().split()))
    if t == 1:
        i, x, y = params
        i -= 1
        w = x+y
        v = x-y
        w_min_seg.set(i, w)
        w_max_seg.set(i, w)
        v_min_seg.set(i, v)
        v_max_seg.set(i, v)
    else:
        L, R, x, y = params
        L -= 1
        R -= 1
        w = x+y
        v = x-y
        
        w_diff = max(abs(w - w_min_seg.prod(L, R+1)), abs(w - w_max_seg.prod(L, R+1)))
        v_diff = max(abs(v - v_min_seg.prod(L, R+1)), abs(v - v_max_seg.prod(L, R+1)))
        ans = max(w_diff, v_diff)
        print(ans)
    
    # print(w_min_seg._d)
    # print(w_max_seg._d)
    # print(v_min_seg._d)
    # print(v_max_seg._d)