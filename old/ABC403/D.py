N, D = list(map(int, input().split()))
A = list(map(int, input().split()))


if D == 0:
    print(N-len(set(A)))
else:
    from collections import defaultdict, Counter

    dd = defaultdict(list)

    for a in A:
        dd[a%D].append(a)

    ans = 0

    for k, v in dd.items():
        # print(k, v)
        counter = Counter(v)
        dp = [[float('inf')]*2 for _ in range((10**6)//D+1)]
        for i in range((10**6)//D+1):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = counter[k]
            else:
                dp[i][0] = dp[i-1][1]
                dp[i][1] = min(dp[i-1]) + counter[k+i*D]
            
        # print(dp[:10])
        
        ans += min(dp[(10**6)//D])
    print(ans)