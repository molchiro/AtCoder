N, M = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, b, c = list(map(int, input().split()))
    G[u-1].append((v-1, b, c))

ok = 0
ng = 10**10

while ng-ok > 0.00000000001:
    m = (ok+ng)/2
    # print(m)
    dp = [-10**10]*N
    dp[0] = 0
    for u in range(N):
        for v, b, c in G[u]:
            dp[v] = max(dp[v], dp[u]+b-c*m)
    
    if dp[-1] >= 0:
        ok = m
    else:
        ng = m

print(ok)