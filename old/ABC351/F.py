N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict
p = defaultdict(list)

for i, a in enumerate(A):
    p[a].append(i)

from atcoder.segtree import SegTree

sum_seg = SegTree(lambda x, y: x+y, 0, A)
bit_seg = SegTree(lambda x, y: x+y, 0, [1]*N)

ans = 0
for k in sorted(p.keys()):
    targets = p[k]
    for t in targets:
        sum_seg.set(t, 0)
        bit_seg.set(t, 0)
    
    for t in targets:
        ans += sum_seg.prod(t, N) - k*bit_seg.prod(t, N)

print(ans)
