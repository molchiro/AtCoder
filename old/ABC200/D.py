N = int(input())
A = list(map(int, input().split()))
# dp[i][q] = [a, b, c...] 
# i: Aをi個目まで見た
# q: 余りが
# a,b,c...: 選んだ要素の選び方
dp = [[None for _ in range(200)] for _ in range(N+1)]
ans = [[] for _ in range(200)]
for i in range(N):
    # 空集合からの追加
    dp[i+1][A[i]%200] = [i+1]
    ans[A[i]%200].append([i+1])
    for j in range(200):
        q = (j+A[i])%200
        if dp[i][j] != None:
            # 選ばない時
            if dp[i+1][j] != []:
                dp[i+1][j] = dp[i][j][:]
            # 選ぶ時
            dp[i+1][q] = dp[i][j] + [i+1]
            ans[q].append(dp[i+1][q])
        if len(ans[q]) >= 2:
            B, C, *_ = ans[q]
            print('Yes')
            print(len(B), *B)
            print(len(C), *C)
            exit()
print('No')