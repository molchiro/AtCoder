INF = 10**18
N, X, Y = list(map(int, input().split()))
dp = [[INF]*(X+2) for _ in range(N+1)]
dp[0][0] = 0

ans = 0
for _ in range(N):
    A, B = list(map(int, input().split()))
    for n in range(N-1, -1, -1):
        for a in range(X):
            if a+A > X:
                continue
            if dp[n][a]+B > Y:
                continue
            dp[n+1][a+A]= min(dp[n+1][a+A], dp[n][a]+B)
            ans = max(ans, n+1)
            
print(min(N, ans+1))