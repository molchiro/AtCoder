from atcoder.fenwicktree import FenwickTree

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
ft = FenwickTree(N)
for i, a in enumerate(A):
    ft.add(i, a)
for _ in range(Q):
    a, b, c = list(map(int, input().split()))
    if a == 0:
        ft.add(b, c)
    else:
        print(ft.sum(b, c))