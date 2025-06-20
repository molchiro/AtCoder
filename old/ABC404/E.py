N = int(input())
C = list(map(int, input().split()))
A = list(map(int, input().split()))

from atcoder.segtree import SegTree
d_seg_tree = SegTree(min, float('inf'), N)
a_seg_tree = SegTree(max, 0, N)

d_seg_tree.set(0, 0)
for i in range(1, N):
    a_seg_tree.set(i, A[i-1])

# print(a_seg_tree._d)

for i in range(1, N):
    c = C[i-1]
    if a_seg_tree.prod(i-c, i):
        x = 0
    else:
        x = d_seg_tree.prod(i-c, i)
    d_seg_tree.set(i, x+1)

# print(d_seg_tree._d)

ans = 0
for i, a in enumerate(A):
    ans += d_seg_tree.get(i+1)*a
print(ans)