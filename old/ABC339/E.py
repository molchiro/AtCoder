N, D = list(map(int, input().split()))
A = list(map(int, input().split()))
from atcoder.segtree import SegTree

seg = SegTree(lambda a, b: max(a, b), 0, 5*10**5+1)
for a in A:
    M = seg.prod(max(0, a-D), min(5*10**5, a+D)+1)
    seg.set(a, M+1)
print(seg.all_prod())