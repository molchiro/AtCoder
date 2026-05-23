from atcoder.modint import Modint, ModContext

mod = 998244353
with ModContext(mod):

    N, M = list(map(int, input().split()))
    edges = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

    from atcoder.dsu import DSU

    dsu = DSU(N)
    ct = 0
    deleted = [0]*M
    for i in range(M-1, -1, -1):
        u, v = edges[i]
        if dsu.same(u, v):
            pass
        elif ct < N-2:
            ct += 1
            dsu.merge(u, v)
        else:                
            deleted[i] = 1

    # print(deleted)


    ans = Modint(0)
    accum = Modint(2)
    for i in range(M):
        if deleted[i]:
            ans += accum
        accum *= 2
    print(ans.val())