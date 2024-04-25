from math import ceil


N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
R = [list(map(int, input().split())) for _ in range(N)]
D = [list(map(int, input().split())) for _ in range(N-1)]

# dp[i][j] = (n: n回待機した, c: 必要なコスト, his:[Piで何回稼ぐか]) ゴールから数えてあと何手のマスか　右から数えていくつめのマスか
inf = 10**18
dp = [[(inf, inf, [])]*N for _ in range(2*N-2)]
dp[0][0] = (0, 0, [])

for i in range(2*N-2):
    for j in range(min(1+i, 2*N-1-i)):
        x = N-1-j
        y = N-1-i+j
        n, c, his = dp[i][j]
        if y > 0:
            # 上に戻る
            u = D[y-1][x]
            p = P[y-1][x]
            v = ceil()
            for a, b in his:

            tmp = (, c+u, )
            if tmp >= hoe
                dp[i+1][j] = tmp

        # 左に戻る