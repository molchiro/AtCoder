from atcoder.dsu import DSU

N, Q = list(map(int, input().split()))

dsu = DSU(N)

toggle = [0]*N
black = [0 for _ in range(N)]

for _ in range(Q):
    t, *rem = list(map(int, input().split()))
    if t == 1:
        u, v = list(map(lambda x: x - 1, rem))

        if dsu.same(u, v):
            continue

        pu = dsu.leader(u)
        pv = dsu.leader(v)

        dsu.merge(u, v)

        if dsu.leader(u) == pu:
            black[pu] += black[pv]
            black[pv] = black[pu]
        else:
            black[pv] += black[pu]
            black[pu] = black[pv]

    elif t == 2:
        v = int(rem[0])-1
        toggle[v] += 1
        toggle[v] %= 2
        if toggle[v] == 0:
            black[dsu.leader(v)] -= 1
        else:
            black[dsu.leader(v)] += 1
    else:
        v = int(rem[0])-1
        print('Yes' if black[dsu.leader(v)] > 0 else 'No')
    