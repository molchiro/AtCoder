from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

N = int(input())
G = [defaultdict(list) for _ in range(N+1)]
leader = [-1]*(N+1)
leader[0] = 0

for i in range(N):
    x, y = list(map(int, input().split()))
    l = leader[x]
    if G[l][y] == []:
        leader[i+1] = i+1
    else:
        leader[i+1] = G[l][y][0]
    G[l][y].append(i+1)


ans = []
def dfs(u):
    global G, ans
    for k in sorted(G[u].keys()):
        for v in G[u][k]:
            ans.append(v)
        dfs(G[u][k][0])
dfs(0)
print(*ans)