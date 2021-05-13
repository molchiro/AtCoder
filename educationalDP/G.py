import sys
sys.setrecursionlimit(10**9)

N, M = list(map(int, input().split()))
G = [[] for _ in range(N)]

for _ in range(M):
    x, y = list(map(lambda x: int(x) - 1, input().split()))
    G[x].append(y)

dp = [-1]*(N)

def f(v):
    if dp[v] != -1:
        return dp[v]
    ans = 0
    for nv in G[v]:
        ans = max(ans, f(nv) + 1)
    dp[v] = ans
    return ans

ans = 0
for i in range(N):
    ans = max(ans, f(i))

print(max(dp))