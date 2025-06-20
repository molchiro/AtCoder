from atcoder.dsu import DSU

N, M = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = list(map(lambda x: int(x) - 1, input().split()))
    G[a].append(b)
    G[b].append(a)

dsu_candidates = DSU(N)
dsu_pure = DSU(N)
s = [set([i]) for i in range(N)]

for i in range(N):
    for v in G[i]:
        if v <= i:
            dsu_pure.merge(i, v)

        if dsu_candidates.same(i, v):
            continue

        i_l = dsu_candidates.leader(i)
        v_l = dsu_candidates.leader(v)

        dsu_candidates.merge(i, v)

        if dsu_candidates.leader(i) == i_l:
            s[i_l] |= s[v_l]
        else:
            s[v_l] |= s[i_l]

    # print(dsu_pure.groups())
    # print(dsu_candidates.groups())
    # print(s)
    
    if dsu_pure.size(0) == i+1:
        print(len(s[dsu_candidates.leader(0)]) - (i+1))
    else:
        print(-1)
