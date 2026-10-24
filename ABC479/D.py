from atcoder.segtree import SegTree

N, Q = list(map(int, input().split()))
L = [10**18] + list(map(int, input().split()))
R = list(map(int, input().split())) + [10**18]
L_seg = SegTree(lambda x, y: min(x, y), 10**18, L)
R_seg = SegTree(lambda x, y: min(x, y), 10**18, R)

for _ in range(Q):
    s, t = list(map(lambda x: int(x) - 1, input().split()))
    if s == N-1:
        print(L[s])
    elif s == 0:
        print(R[s])
    elif s < t:
        # 直接右と左いって右
        print(min(R[s], L[s] + R_seg.prod(0, s)))
    else:
        # 直接左と右いって左
        print(min(L[s], R[s] + L_seg.prod(s+1, N)))

