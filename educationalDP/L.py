N = int(input())
A = list(map(int, input().split()))

dp = [[0]*(N+1) for _ in range(N+1)]

for n in range(1, N+1):
    for l in range(0, N-n+1):
        r = l + n
        if (N-n)%2==0:
            dp[l][r] = max(dp[l+1][r] + A[l], dp[l][r-1] + A[r-1])
        else:
            dp[l][r] = min(dp[l+1][r] - A[l], dp[l][r-1] - A[r-1])
print(dp[0][N])