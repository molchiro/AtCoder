T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    dp = [10**18]*2
    if S[0] == 'S':
        dp = [0, -X[0]]
    else:
        dp = [-X[0], 0]


    for i in range(1, N):
        ndp = [-10**18]*2

        if S[i] == 'S':
            # 晴れのまま
            ndp[0] = max(ndp[0], dp[0], dp[1]+Y[i-1])
            # 雨に変える
            ndp[1] = max(ndp[1], dp[0]-X[i], dp[1]-X[i])
        else:
            # 晴れに変える
            ndp[0] = max(ndp[0], dp[0]-X[i], dp[1]+Y[i-1]-X[i])
            # 雨のまま
            ndp[1] = max(ndp[1], dp[0], dp[1])
        dp = ndp
    
    print(max(dp))