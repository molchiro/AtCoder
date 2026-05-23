N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))

from atcoder.segtree import SegTree

B = [0]*(5*(10**5)+1)
C = [0]*(5*(10**5)+1)
for a in A:
    B[a] += 1
    C[a] += a
# print(B[:10])
# print(C[:10])
seg_B = SegTree(lambda x, y: x+y, 0, B)
seg_C = SegTree(lambda x, y: x+y, 0, C)

for _ in range(Q):
    t, *params = list(map(int, input().split()))
    if t == 1:
        x, y = params
        x -= 1
        prev = A[x]
        A[x] = y
        # B[prev] -= 1
        # B[y] += 1
        # C[prev] -= prev
        # C[y] += y
        # print(B[:10])
        # print(C[:10])
        seg_B.set(prev, seg_B.get(prev)-1)
        seg_B.set(y, seg_B.get(y)+1)
        seg_C.set(prev, seg_C.get(prev)-prev)
        seg_C.set(y, seg_C.get(y)+y)
    else:
        l, r = params
        if l >= r:
            print(l*N)
        else:
            ans = seg_B.prod(0, l)*l + seg_C.prod(l, r) + seg_B.prod(r, 5*(10**5)+1)*r
            # print(seg_B.prod(0, l)*l , seg_C.prod(l, r), seg_B.prod(r, 5*(10**5)+1)*r)
            print(ans)