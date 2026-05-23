import sys
sys.setrecursionlimit(10**9)


Q = int(input())
for _ in range(Q):
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = list(map(lambda x: int(x) - 1, input().split()))
        G[a].append(b)
        G[b].append(a)
    
    degree = [len(G[i]) for i in range(N)]

    seen = [0]*N

    # returns (自分を含んで3,4,,,が続いている),  (3,4,4,4,4,3で終わっている)
    def dfs(u):
        global seen, G, degree
        seen[u] = 1
        countinuous_top = [0, 0] # 子の部分木の中で3,4,4,,,と続いている部分の最大値（二位まで）
        closed_top = 0 # 子の部分木の中で3,4,4,,,3と完成済みの中の最大値
        for v in G[u]:
            if seen[v]:
                continue
            continuous, closed = dfs(v)
            closed_top = max(closed_top, closed)
            countinuous_top = sorted([continuous] + countinuous_top, reverse=True)[:2]
        
        # print(u, countinuous_top)
            

        # 子の部分木に自分を加えた情報を返す
        if degree[u] == 3:
            return 1, max(closed_top, countinuous_top[0]+1)
        elif degree[u] > 3:
            return countinuous_top[0]+1, max(closed_top, sum(countinuous_top)+1)
        else:
            return 0, closed_top
        
    
    print(max(max(dfs(0)), 1))