N = int(input())
A = list(map(int, input().split()))

inf = 10**18

dp = [0, -inf]
for a in A:
    dp = [max(dp[0], dp[1] + a*2), max(dp[1], dp[0] + a)]
print(max(dp))