N = int(input())
P = list(map(int, input().split()))

from atcoder.segtree import SegTree

seg = SegTree(lambda x, y:x+y, 0, [0]*N)

ans = 0
for i in range(N):
    v = P[i]
    seg.set(v-1, 1)
    ans += v - seg.prod(0, v)
    print(ans)
print(ans)