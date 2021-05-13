N, X = list(map(int, input().split()))
A = ['dummy'] + list(map(int, input().split()))

# dp[i][j][k]
# i: i番目まで見た
# j: j個選んだ
# k: jで割ったあまりがk
dp = [[[0]*N for _ in range(N+1)] for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        for k in range(N):
            # i+1番目を選ぶ
            new_val = dp[i][j][k] + A[i+1]
            # print(i+1, j+1, new_val%(j+1), dp[i+1][j+i][new_val%(j+1)])
            dp[i+1][j+1][new_val%(j+1)] = max(new_val, dp[i+1][j+1][new_val%(j+1)])
            # i+1番目を選ばない
            dp[i+1][j][k] = max(dp[i][j][k], dp[i+1][j][k])

print(*dp, sep='\n')
ans = N*X
for j in range(1, N+1):
    k = X%j
    print(N, j, k)
    if dp[N][j][k] == 0:
        continue
    ans = min((X-dp[N][j][k])//j, ans)

print(ans)