N = int(input())
S = input()
T = input()

# dp[i][j] = iラウンドまでで確定している数字の余りがjであるとき、高橋くんが勝つなら1 else 0
dp = [[0]*7 for _ in range(N+1)]
dp[N][0] = 1
for i in range(N, 0, -1):
    Ti = T[i-1]
    Si = int(S[i-1])
    for j in range(7):
        if Ti == 'T':
            dp[i-1][j] = dp[i][(j*10 + Si)%7] or dp[i][(j*10)%7]
        else:
            dp[i-1][j] = dp[i][(j*10 + Si)%7] and dp[i][(j*10)%7]
if dp[0][0]:
    print('Takahashi')
else:
    print('Aoki')