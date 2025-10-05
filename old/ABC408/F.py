from atcoder.segtree import SegTree
from collections import deque

N, D, R = list(map(int, input().split()))
H = list(map(int, input().split()))
d = {}
for i, h in enumerate(H):
    d[h-1] = i

seg = SegTree(max, -1, [-1]*N)

dq = deque([])
for h in range(D):
    dq.append((d[h], 0))

ans = 0
for h in range(D, N):
    u, v = dq.popleft()
    seg.set(u, v)

    tmp = seg.prod(max(0, d[h]-R), min(N, d[h]+R+1)) + 1
    ans = max(ans, tmp)
    dq.append((d[h], tmp))

print(ans)