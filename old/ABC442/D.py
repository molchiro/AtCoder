N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))


from atcoder.segtree import SegTree
seg = SegTree(lambda x, y: x+y, 0, A)
for _ in range(Q):
    t, *params = list(map(int, input().split()))
    if t == 1:
        x = params[0]-1
        l = seg.get(x)
        r = seg.get(x+1)
        seg.set(x+1, l)
        seg.set(x, r)
    else:
        l, r = params
        l -= 1
        print(seg.prod(l, r))