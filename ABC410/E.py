N, H, M = list(map(int, input().split()))
dp = [-1]*(H+1)
dp[H] = M
for i in range(N):
    ndp = [-1]*(H+1)
    A, B = list(map(int, input().split()))
    f = 0
    for h in range(H+1):
        if dp[h] == -1:
            continue

        if h >= A:
            ndp[h-A] = max(ndp[h-A], dp[h])
            f = 1
        if dp[h] >= B:
            ndp[h] = max(ndp[h], dp[h]-B)
            f = 1

    if f == 0:
        print(i)
        break
    dp = ndp
    # print(dp)
else:
    print(N)