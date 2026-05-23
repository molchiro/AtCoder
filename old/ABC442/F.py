N = int(input())

dp = [0]*(N+1)
for _ in range(N):
    S = input()

    # 黒マスの累積和
    cumsum = [0]
    for s in S:
        cumsum.append(cumsum[-1] + (int(s == '#')))
    # print(cumsum)
    ndp = [10**18]*(N+1)
    tmp = 10**18
    for i in range(N, -1, -1):
        tmp = min(tmp, dp[i])
        toggle_white = cumsum[i]-cumsum[0]
        toggle_black = (N-i - (cumsum[N]-cumsum[i]))
        n = toggle_white + toggle_black
        ndp[i] = min(ndp[i], tmp+n)
    dp = ndp
    # print(dp)

print(min(dp))