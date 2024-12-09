from atcoder.segtree import SegTree
from bisect import bisect_left, bisect_right

N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))

segtree = SegTree(lambda x, y: x+y, 0, P)

Q = int(input())
for _ in range(Q):
    L, R = list(map(int, input().split()))
    l = bisect_left(X, L)
    r = bisect_right(X, R)
    # print(l, r)
    print(segtree.prod(l, r))