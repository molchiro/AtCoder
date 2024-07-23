N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

from atcoder.lazysegtree import LazySegTree

def op(a, b):
    return max(a, b)
e = 0
def mapping(f, x):
    return f+x
def composition(f, g):
    return f+g

id = 0
seg = LazySegTree(op, e, mapping, composition, id, A)
for b in B:
    n = seg.prod(b, b+1)
    seg.set(b, 0)
    b += 1
    b %= N
    while n > 0:
        if b == 0 and n >= N:
            c = n//N
            seg.apply(0, N, c)
            n -= c*N
        elif N - b <= n:
            seg.apply(b, N, 1)
            n -= N-b
            b = 0
        else:
            seg.apply(b, b+n, 1)
            n = 0

ans = []
for i in range(N):
    ans.append(seg.prod(i, i+1))
print(*ans, sep=' ')


# for i in range(Q):
#     t, l, r = mi()
#     l -= 1
#     if t == 1:
#         seg.apply(l, r, 0)
#     else:
#         ans = seg.prod(l,r)
#         print(ans[2])

