N = int(input())
P = list(map(int, input().split()))
dp = [0]*(N+1)
for i, p in enumerate(P):
    dp_prev = dp[:]
    dp = [0]*(N+1)
    for j in range(i+1):
        # 取る
        dp[j+1] = max(dp[j+1], dp_prev[j]*0.9 + p)
        # 取らない
        dp[j] = max(dp[j], dp_prev[j])

ans = -float('inf')
sigma = 0
for k in range(1, N+1):
    sigma += 0.9**(k-1)
    ans = max(ans, dp[k]/sigma - 1200/(k**0.5))
print(ans)