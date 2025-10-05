N = int(input())
T = input()

# dp[i][b]: i番目が右端になるようなTの部分文字列の中で、唯一残った文字をbにすることができる
dp = [[0]*2 for _ in range(N)]

if T[0] == '0':
    dp[0][0] = 1
else:
    dp[0][1] = 1

for i in range(1, N):
    if T[i] == '0':
        dp[i][0] += dp[i-1][1] + 1
        dp[i][1] += dp[i-1][0]
    else:
        dp[i][1] += dp[i-1][1] + 1
        dp[i][0] += dp[i-1][0]

# print(dp)

ans = 0
for i in range(N):
    ans += dp[i][1]
print(ans)