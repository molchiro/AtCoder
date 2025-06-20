dp = ["1"*(10**6)]*(2001)
dp[1] = '1'
dp[11] = '11'
dp[111] = '111'
dp[1111] = '1111'

for i in range(1, 1999):
    for j in range(1, i+1):
        if i+j > 2000 and i*j > 2000:
            break

        # i + j
        if i+j <= 2000:
            if len(dp[i]) + len(dp[j]) + 1 < len(dp[i+j]):
                expr = dp[i] + "+" + dp[j]
                x = eval(expr)
                dp[x] = expr

        # (i)*(j)
        if i*j <= 2000:
            n = len(dp[i]) + len(dp[j]) + 5
            if i in [1, 11, 111, 1111]:
                n -= 2
            if j in [1, 11, 111, 1111]:
                n -= 2

            
            if n < len(dp[i*j]):

                if i in [1, 11, 111, 1111]:
                    l = str(i)
                else:
                    l = "(" + dp[i] + ")" if '+' in dp[i] else dp[i]

                if j in [1, 11, 111, 1111]:
                    r = str(j)
                else:
                    r = "(" + dp[j] + ")" if '+' in dp[j] else dp[j]

                expr = l + '*' + r
                x = eval(expr)
                dp[x] = expr

# print('ready')

N = int(input())
print(dp[N])