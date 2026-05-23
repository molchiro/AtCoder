N, K = list(map(int, input().split()))
P = list(map(int, input().split()))

from atcoder.segtree import SegTree

seg = SegTree(lambda x, y: x+y, 0, N)

tmp = 0
l = -1
ans = 0
for i, p in enumerate(P):
    seg.set(p-1, 1)
    tmp += i+1 - seg.prod(0, p)
    print(tmp)
    while tmp > K:
        l += 1
        tmp -= seg.prod(0, P[l]-1)
    print('minused', tmp)
    
    if tmp == K:
        ans += max(i-l-K+1, 0)
    # print(tmp, i, l)
    
print(ans)