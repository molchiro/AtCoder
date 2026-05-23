N = int(input())
S = input()
d = {'A': 1, 'B': -1, 'C': 0}
T = [d[s] for s in S]
# print(T)
cumsum = [0]
for t in T:
    cumsum.append(cumsum[-1]+t)
cumsum = cumsum[1:]
# print(cumsum)

from collections import Counter

counter = Counter(cumsum)
# print(counter)

ct_min = min(cumsum)
from atcoder.segtree import SegTree
l = [(k, v) for k, v in counter.items()]
l.sort()
l = [v for _, v in l]
# print(l)
seg = SegTree(lambda x, y: x+y, 0, l)

ans = 0
border = 1
for i in range(N):
    t = T[i]
    idx = border - ct_min
    if idx <= len(l):
        ans += seg.prod(idx, len(l))
    # print(t, border, idx, ans)
    border += t
    v = cumsum[i]-ct_min
    seg.set(v, seg.get(v)-1, )
print(ans)