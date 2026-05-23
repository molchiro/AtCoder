mod = 998244353
inv_2 = pow(2, mod - 2, mod)

N, Q = list(map(int, input().split()))

from atcoder.lazysegtree import LazySegTree

e = (1, 0, 0) # (size, weigth, weight^2)
id = 0
def op(a, b):
    sa, wa, wwa = a
    sb, wb, wwb = b
    size = sa + sb
    weight = wa + wb
    weiwei = wwa + wwb
    return (size%mod, weight%mod, weiwei%mod)
def mapping(f, x):
    s, w, ww = x
    size = s
    weight = w + s*f
    weiwei = ww + 2*f*w + s*f*f
    return (size%mod, weight%mod, weiwei%mod)
def composition(f, g):
    return (f+g)%mod

seg = LazySegTree(op, e, mapping, composition, id, [(1, 0, 0) for _ in range(N)])

for _ in range(Q):
    l, r, a = list(map(int, input().split()))
    seg.apply(l-1, r, a)
    _, w, ww = seg.prod(l-1, r)
    print((w*w - ww)*inv_2%mod)