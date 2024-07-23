N, Q = list(map(int, input().split()))
S = input() + '2' # 右端に番兵を挿入
T = [int(S[i+1] != S[i]) for i in range(N)]
# print(T)
from atcoder.segtree import SegTree

seg = SegTree(lambda x, y: x+y, 0, T)

for _ in range(Q):
    t, L, R = list(map(int, input().split()))
    if t == 1:
        if L > 1:
            seg.set(L-2, 1 - seg.get(L-2))
        if R < N:
            seg.set(R-1, 1 - seg.get(R-1))
        # print(*[seg.get(i) for i in range(N)])
    else:
        print('Yes' if seg.prod(L-1, R-1) == R-L else 'No')
            
# 01010
# 11111
# 01110
# 10011
