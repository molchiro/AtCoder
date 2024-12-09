N, M, K = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(M)]
E = list(map(int, input().split()))

dp = [float('inf')]*N
dp[0] = 0

for e in E:
    a, b, c = edges[e-1]
    a -= 1
    b -= 1
    dp[b] = min(dp[b], dp[a]+c)

ans = dp[-1]
if ans == float('inf'):
    ans = -1
print(ans)