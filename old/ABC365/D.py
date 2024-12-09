N = int(input())
S = input()

dp = [[0]*(3) for _ in range(N+1)]
janken = {'R': 0, 'P': 1, 'S': 2}
kati = {0: 1, 1: 2, 2: 0}

for i in range(N):
    s = S[i]
    aoki = janken[s]
    for j in range(3): #直前に出した手
        # かつ
        if j != kati[aoki]:
            dp[i+1][kati[aoki]] = max(dp[i+1][kati[aoki]], dp[i][j] + 1)
        # あいこ
        if j != aoki:
            dp[i+1][aoki] = max(dp[i+1][aoki], dp[i][j])


print(max(dp[-1]))