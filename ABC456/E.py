from atcoder.scc import SCCGraph

T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    
    raw_edges = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
    for i in range(N):
        raw_edges.append((i, i))
    W = int(input())
    holidays = [input() for _ in range(N)]
    # print(holidays)

    scc = SCCGraph(N*W)
    for u, v in raw_edges:
        for w in range(W):
            nw = (w+1)%W

            if holidays[u][w] == 'o' and holidays[v][nw] == 'o':
                scc.add_edge(u*W+w, v*W+nw)

            if holidays[v][w] == 'o' and holidays[u][nw] == 'o':
                scc.add_edge(v*W+w, u*W+nw)
        
    # print(scc.scc())
    
    f = 0
    for group in scc.scc():
        if len(group) > 1:
            f = 1
    print('Yes' if f else 'No')
