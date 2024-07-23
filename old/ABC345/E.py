N, K = list(map(int, input().split()))
BALLS = [(-1, 0)] + [tuple(map(int, input().split())) for _ in range(N)] + [(-1, 0)]
N += 1
# dp[i][j]: 最後に選んだボールがi番目で、取り除いた数がj個である
inf = 10**18
dp = [[-inf]*(K+1) for _ in range(N+1)]
dp[0][0] = 0

for now in range(N):
    for j in range(K+1):
        # k: 何個スキップするか
        for k in range(K-j+1):
            nxt = now+k+1
            if nxt > N:
                break
            if BALLS[now][0] == BALLS[nxt][0]:
                continue
            dp[nxt][j+k] = max(dp[nxt][j+k], dp[now][j]+BALLS[nxt][1])

    # print(dp)
ans = dp[-1][-1]

if ans == -inf:
    ans = -1

print(ans)