from sortedcontainers import SortedList

INF = 10**18
N, Q = list(map(int, input().split()))

pos = []
sortedlist_z = []
sortedlist_w = []
for _ in range(N):
    x, y = list(map(int, input().split()))
    pos.append((x-y, x+y))
    sortedlist_z.append(SortedList([-INF, x-y, INF]))
    sortedlist_w.append(SortedList([-INF, x+y, INF]))

from atcoder.dsu import DSU

dsu = DSU(2*N)

def dist(sortedlist_z_u, sortedlist_z_v, sortedlist_w_u, sortedlist_w_v):
    min_z = float('inf')
    idx = 0
    for z in sortedlist_z_u[1:len(sortedlist_z_u)-1]:
        while z > sortedlist_z_v[idx]:
            idx += 1
        min_z = min(min_z, abs(z - sortedlist_z_v[idx-1]), abs(z - sortedlist_z_v[idx]))

    min_w = float('inf')
    idx = 0
    for w in sortedlist_w_u[1:len(sortedlist_w_u)-1]:
        while w > sortedlist_w_v[idx]:
            idx += 1
        min_w = min(min_w, abs(w - sortedlist_w_v[idx-1]), abs(w - sortedlist_w_v[idx]))

    return max(min_z, min_w)

for _ in range(Q):
    query = input()
    if query[0] == '1':
        _, a, b = list(map(lambda x: int(x), query.split()))
        pos.append((a-b, a+b))
        sortedlist_z.append(SortedList([-INF, a-b, INF]))
        sortedlist_w.append(SortedList([-INF, a+b, INF]))
        N += 1    
    elif query[0] == '2':

        leaders = list(set([dsu.leader(i) for i in range(N)]))
        if len(leaders) == 1:
            print(-1)
            continue

        edges = []
        for i in range(len(leaders)-1):
            u = leaders[i]
            for j in range(u+1, len(leaders)):
                v = leaders[j]
                d = dist(sortedlist_z[u], sortedlist_z[v], sortedlist_w[u], sortedlist_w[v])
                edges.append((d, (u, v)))
        
        edges.sort()
        k = edges[0][0]

        for d, (u, v) in edges:
            if d > k:
                break

            dsu.merge(u, v)

            slzu = sortedlist_z[u]
            slzv = sortedlist_z[v]

            if len(slzu) < len(slzv):
                slzu, slzv = slzv, slzu
            
            tmp_z = slzu
            for a in slzv[1:len(slzv)-1]:
                tmp_z.add(a)
            sortedlist_z[u] = sortedlist_z[v] = tmp_z

            slwu = sortedlist_w[u]
            slwv = sortedlist_w[v]

            if len(slwu) < len(slwv):
                slwu, slwv = slwv, slwu
            
            tmp_w = slwu
            for a in slwv[1:len(slwv)-1]:
                tmp_w.add(a)
            sortedlist_w[u] = sortedlist_w[v] = tmp_w


        print(k)


    else:
        _, u, v = list(map(lambda x: int(x) - 1, query.split()))
        print('Yes' if dsu.same(u, v) else 'No')
