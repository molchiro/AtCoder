Q, V = list(map(int, input().split()))


from atcoder.lazysegtree import LazySegTree

INF = 1 << 63

# 区間最大値管理,区間和
def op(ele1, ele2):
    if ele1[0] > ele2[0]:
        return ele1
    else:
        return ele2

def mapping(func, ele):
    return (ele[0]+func, ele[1])

def composition(func_upper, func_lower):
    return func_upper + func_lower

e = (-INF, -1)
id_ = 0

seg = LazySegTree(op, e, mapping, composition, id_, 300005)

prev = 0
for q in range(Q):
    type, *params = list(map(int, input().split()))
    if type == 1:
        t, w = params
        seg.apply(0, 300005, t-prev)
        seg.set(q, (w, q))

    else:
        t = params[0]
        seg.apply(0, 300005, t-prev)
        M, idx = seg.prod(0, 300005)
        if M < 0:
            print(-1)
        else:
            print(min(M, V))
            seg.set(idx, (-INF, idx))


    prev = t