N = int(input())
S = input()
C = list(map(int, input().split()))

# dp[i][j][k]: i文字目まで見て、同じ文字が連続する箇所がjこ（最大3) 直前が0か1か
dp = [[[10**18]*2 for _ in range(3)] for _ in range(N+1)]
dp[0][0][1] = 0
dp[0][0][0] = 0
for i in range(N):
    s = S[i]
    for j in range(3):
        for k in range(2):
            if i > 0:
                if s == '0':
                    # 操作しない
                    dp[i+1][min(2,j+int(k==0))][0] = min(dp[i+1][min(2,j+int(k==0))][0], dp[i][j][k])
                    # 操作する
                    dp[i+1][min(2,j+int(k==1))][1] = min(dp[i+1][min(2,j+int(k==1))][1], dp[i][j][k]+C[i])
                else:
                    # 操作しない
                    dp[i+1][min(2,j+int(k==1))][1] = min(dp[i+1][min(2,j+int(k==1))][1], dp[i][j][k])
                    # 操作する
                    dp[i+1][min(2,j+int(k==0))][0] = min(dp[i+1][min(2,j+int(k==0))][0], dp[i][j][k]+C[i])
            else:
                if s == '0':
                    # 操作しない
                    dp[i+1][min(2,j)][0] = min(dp[i+1][min(2,j)][0], dp[i][j][k])
                    # 操作する
                    dp[i+1][min(2,j)][1] = min(dp[i+1][min(2,j)][1], dp[i][j][k]+C[i])
                else:
                    # 操作しない
                    dp[i+1][min(2,j)][1] = min(dp[i+1][min(2,j)][1], dp[i][j][k])
                    # 操作する
                    dp[i+1][min(2,j)][0] = min(dp[i+1][min(2,j)][0], dp[i][j][k]+C[i])
    # print(dp[i+1])
            

print(min(dp[-1][1]))