H, N = list(map(int, input().split()))
magics = [list(map(int, input().split())) for _ in range(N)]

dp = [float('inf')]*(H+10000)

dp[0] = 0

for i in range(H):
    for A, B in magics:
        dp[i+A] = min(dp[i+A], dp[i]+B)

print(min(dp[H:]))