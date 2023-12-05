MOD = 998244353
Q, K = list(map(int, input().split()))
dp = [0]*5002
dp[0] = 1
for _ in range(Q):
    query, x = input().split()
    x = int(x)
    if query == '+':
        for i in range(5001):
            dp[min(5001, 5000-i+x)] += dp[5000-i]
            dp[min(5001, 5000-i+x)] %= 998244353
    else:
        for i in range(5001):
            dp[min(5001, i+x)] -= dp[i]
            dp[min(5001, i+x)] %= MOD
    # print(dp[:K+1])
    print(dp[K])