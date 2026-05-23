S = input()
T = input()

N = len(S)

if len(T) == 1:
    l = S.split(T)
    ans = 0
    for e in l:
        ans += len(e)*(len(e)+1)//2
    print(ans)
else:
    # dp[i]: Tのi文字目までを含んだ部分文字列が作れる時の左端位置が一番右
    dp = [10**18]*len(T)

    ng_ranges = []

    for i, s in enumerate(S):

        if s == T[-1] and dp[-1] != dp[-2]:
            # print(i)
            dp[-1] = dp[-2]
            ng_ranges.append(((dp[-1]), (i)))

        for j in range(len(T)-2, 0, -1):
            if s == T[j]:
                dp[j] = dp[j-1]

        if s == T[0]:
            dp[0] = i
    
    ng_ranges.append((N+1,N))
        
    # print(ng_ranges)

    ng_ranges = ng_ranges[::-1]

    ans = 0

    for i in range(N):
        if ng_ranges[-1][0] < i:
           ng_ranges.pop()
        ans += ng_ranges[-1][1] - i
        # print(ans)

    print(ans)