from atcoder.dsu import DSU

N, Q = list(map(int, input().split()))
dsu = DSU(N)
for _ in range(Q):
    t, u, v = list(map(int, input().split()))
    if t == 0:
        dsu.merge(u, v)
    else:
        print(int(dsu.same(u, v)))