from atcoder.modint import Modint, ModContext
from atcoder.lazysegtree import LazySegTree

mod = 998244353
with ModContext(mod):


    N = int(input())
    inv_6 = Modint(6).inv()

    A = [list(map(int, input().split())) for _ in range(N)]
    A_set = set()
    for aa in A:
        for a in aa:
            A_set.add(a)
    A_set.add(0)
    A_list = sorted(list(A_set))
    A_dict = {v: i for i, v in enumerate(A_list)}
    print(A_dict)

    def op(x, y):
        return lambda x, y: x + y
    e = Modint(0)
    def mapping(f, x):
        return f*x
    def composition(f, g):
        return f*g
    id = Modint(1)

    # seg = LazySegTree(op, Modint(0), [Modint(0) for _ in range(6*N+1)])
    seg = LazySegTree(op, e, mapping, composition, id, [Modint(0) for _ in range(6*N+1)])
    seg.set(0, Modint(1))
    for aa in A:
        aaa = sorted(aaa)
        aaa = [-1] + aaa
        n = 0
        while aaa:
            x = aaa.pop()
            n += 1
            m = 1
            if x == -1:
                break

            while aaa and aaa[-1] == x:
                x = aaa.pop()
                n += 1
                m += 1
            
            # 目の位置を更新
            idx = A_dict[x]
            x = seg.prod(0, idx+1) * Modint(m) / inv_6
            seg.set(idx, x)
            # 目と次の間を更新
            if aaa[-1] == -1:
                n_idx = -1
            else:
                n_idx = A_dict[aaa[-1]]
            seg.apply(n_idx+1, idx, Modint(6-n) * inv_6)
            


    
    ans = Modint(0)
    for idx in range(N+1):
        ans += Modint(A_list[idx]) * seg.get(idx)
    print(ans.val())



