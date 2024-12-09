N, K = list(map(int, input().split()))
l = [list(map(int, input().split())) for _ in range(N)]
l.sort(key=lambda x: (x[0]-1)/x[1])


dp = [0]*(K+1)
dp[0] = 1
for A, B in l:
    ndp = dp[:]
    for k in range(K):
        if dp[k] == 0:
            continue
        ndp[k+1] = max(ndp[k+1], dp[k]*A+B)
    dp = ndp
    # print(dp)

print(dp[K])