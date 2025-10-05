INF = 1 << 63

N = int(input())
A = list(map(int, input().split()))

Q = int(input())

from atcoder.segtree import SegTree
from atcoder.lazysegtree import LazySegTree


# 区間最小値管理
def op(ele1, ele2):
    if ele1[0] < ele2[0]:
        return ele1
    else:
        return ele2

def mapping(func, ele):
    return (ele[0]+func, ele[1])

def composition(func_upper, func_lower):
    return func_upper + func_lower

e = (INF, 0)
id_ = 0

min_seg = LazySegTree(op, e, mapping, composition, id_, [(a, i) for i, a in enumerate(A)])

# 在庫切れ管理
out_of_stock_seg = SegTree(lambda x, y: x+y, 0, N)

for _ in range(Q):
    l, r, k = list(map(int, input().split()))
    l -= 1
    r -= 1

    # 残りk個以下の商品を先に処理
    ans = 0
    while min_seg.prod(l, r+1)[0] <= k:
        x, idx = min_seg.prod(l, r+1)
        ans += x
        out_of_stock_seg.set(idx, 1)
        min_seg.set(idx, (INF, idx))

    # k個買えるのは在庫切れしていない商品
    ans += k*((r-l+1) - out_of_stock_seg.prod(l, r+1))
    print(ans)

    # k個減らす
    min_seg.apply(l, r+1, -k)