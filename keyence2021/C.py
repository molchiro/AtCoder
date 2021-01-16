H, W, K = list(map(int, input().split()))
field = [['']*W for _ in range(H)]
for _ in range(K):
    h, w, c = input().split()
    h, w = int(h)-1, int(w)-1
    field[h][w] = c

# [R, D, X]
dp = [[0, 0, 0]]*((H+1)*(W+1))
if field[0][0] == 'R':
    dp[W+2] = [1, 0, 0]
elif field[0][0] == 'D':
    dp[W+2] = [0, 1, 0]
elif field[0][0] == 'X':
    dp[W+2] = [0, 0, 1]
else:
    dp[W+2] = [1, 1, 1]

# print(dp)
for h in range(1, H+1):
    for w in range(1, W+1):
        # print(h, w)
        if h == 1 and w == 1:
            continue
        n = dp[(W+1)*(h-1) + w][1] + dp[(W+1)*(h-1) + w][2] + dp[(W+1)*h + w-1][0] + dp[(W+1)*h + w-1][2]
        n %= 998244353
        cell = field[h-1][w-1]
        if cell == 'R':
            dp[(W+1)*h + w] = [n, 0, 0]
        elif cell == 'D':
            dp[(W+1)*h + w] = [0, n, 0]
        elif cell == 'X':
            dp[(W+1)*h + w] = [0, 0, n]
        else:
            dp[(W+1)*h + w] = [n, n, n]
            for i in range((W+1)*h + w - W-1, (W+1)*h + w):
                dp[i][0] *= 3
                dp[i][1] *= 3
                dp[i][2] *= 3

# print(dp)
print(sum(dp[-1])%998244353)