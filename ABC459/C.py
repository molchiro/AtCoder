N, Q = list(map(int, input().split()))

from atcoder.segtree import SegTree

offset = 0
seg_min = SegTree(lambda x,y: min(x, y), 10**18, [0]*N)
seg_y = SegTree(lambda x,y: x+y, 0, 10**6)
seg_y.set(0, N)
n = [0]*N

for q in range(Q):
    t, k = list(map(int, input().split()))
    # print(q, offset, seg_min._d)
    if t == 1:
        i = k-1
        prev = n[i]
        n[i] += 1
        seg_y.set(prev, seg_y.get(prev)-1)
        seg_y.set(prev+1, seg_y.get(prev+1)+1)

        seg_min.set(i, n[i])
        if seg_min.all_prod() > offset:
            offset += 1
    else:
        print(seg_y.prod(k+offset, 10**6))

