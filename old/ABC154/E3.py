N = int(input())
K = int(input())
S = str(N)
L = len(S)
# [上から何桁目][1~9を選んだ回数][N未満フラグ]
dp = [[[0]*2 for _ in range(K+1)] for _ in range(L+1)]
dp[0][0][0] = 1
for i in range(L):
    D = int(S[i])
    for k in range(K+1):
        for f in range(2):
            for d in range(10):
                ni = i+1
                nk = k 
                nf = f
                if d != 0:
                    nk += 1
                if nk > K:
                    continue
                if f == 0:
                    if d > D:
                        continue
                    elif d < D:
                        nf = 1
                dp[ni][nk][nf] += dp[i][k][f]
print(dp[L][K][0]+dp[L][K][1])