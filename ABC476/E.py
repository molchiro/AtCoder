N, M = list(map(int, input().split()))
P = list(map(int, input().split()))

from atcoder.segtree import SegTree


min_seg = SegTree(lambda x, y: x if x[0] < y[0] else y, (10**18, -1), [(P[i], i) for i in range(N)])
max_seg = SegTree(lambda x, y: x if x[0] > y[0] else y, (0, -1),[(P[i], i) for i in range(N)])

for _ in range(M):
    L, R = list(map(lambda x: int(x) - 1, input().split()))
    min_val, min_idx = min_seg.prod(L, R+1)
    max_val, max_idx = max_seg.prod(L, R+1)
    # print(_, (min_val, min_idx), (max_val, max_idx))
    min_seg.set(min_idx, (max_val, min_idx))
    min_seg.set(max_idx, (min_val, max_idx))
    max_seg.set(min_idx, (max_val, min_idx))
    max_seg.set(max_idx, (min_val, max_idx))
    P[min_idx] = max_val
    P[max_idx] = min_val


print(*P)