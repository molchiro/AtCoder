import sys
sys.setrecursionlimit(10**9)

T = int(input())
# ct = 0
for _ in range(T):
    N, M, X, Y = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = list(map(lambda x: int(x) - 1, input().split()))
        G[a].append(b)
        G[b].append(a)
    for i in range(N):
        G[i].sort(reverse=True)

    ans = []
    seen = set()
    stack = [X]
    def solve(u):
        # global ct
        # ct += 1
        # print(ct)
        global G, N, M, X, Y
        global ans, seen

        
        ans.append(u)
        seen.add(u)
        if u == Y:
            return True
        while G[u-1]:
            v = G[u-1].pop()
            if v+1 in seen:
                continue
            if solve(v+1):
                return True
        ans.pop()
        seen.remove(u)
        return

    solve(X)
    print(*ans)