N = int(input())
balls = [[] for _ in range(N+1)]
for _ in range(N):
    X, C = list(map(int, input().split()))
    balls[C-1].append(X)
balls[N].append(0)

# dp[i][j] = 色iまで見て、左端で終わったらj==0,右ならj==1
dp = [[float('inf')]*2 for _ in range(N+2)]
dp[0][0] = 0
dp[0][1] = 0
prev_l = 0
prev_r = 0
for i in range(N+1):
    if len(balls[i]) == 0:
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = dp[i][1]
        continue
    l = min(balls[i])
    r = max(balls[i])
    dp[i+1][0] = min(dp[i][0] + abs(prev_l-r), dp[i][1] + abs(prev_r-r)) + r-l
    dp[i+1][1] = min(dp[i][0] + abs(prev_l-l), dp[i][1] + abs(prev_r-l)) + r-l
    prev_l = l
    prev_r = r
print(min(dp[N+1]))