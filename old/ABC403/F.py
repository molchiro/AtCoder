dp = ["1"*100 for _ in range(2001)]
dp[1] = '1'
dp[11] = '11'
dp[111] = '111'
dp[1111] = '1111'

for i in range(1, 2000):
    for j in range(1, i+1):
        if i+j > 2000 and i*j > 2000:
            break

        # i + j
        if i+j <= 2000:
            if len(dp[i]) + len(dp[j]) + 1 < len(dp[i+j]):
                dp[i+j] = dp[i] + "+" + dp[j]

        # (i)*(j)
        if i*j <= 2000:
            if eval(dp[i] + "*" + dp[j]) == i*j:
                if len(dp[i]) + len(dp[j]) + 1 < len(dp[i*j]):
                    dp[i*j] = dp[i] + "*" + dp[j]
            elif eval("(" + dp[i] + ")" + "*" + dp[j]) == i*j:
                if len(dp[i]) + len(dp[j]) + 3 < len(dp[i*j]):
                    dp[i*j] = "(" + dp[i] + ")" + "*" + dp[j]
            elif eval("(" + dp[j] + ")" + "*" + dp[i]) == i*j:
                if len(dp[i]) + len(dp[j]) + 3 < len(dp[i*j]):
                    dp[i*j] = "(" + dp[j] + ")" + "*" + dp[i]
            else:
                if len(dp[i]) + len(dp[j]) + 5 < len(dp[i*j]):
                    dp[i*j] = "(" + dp[j] + ")" + "*" +  "(" + dp[i] + ")"


# print('ready')

N = int(input())
print(dp[N])

