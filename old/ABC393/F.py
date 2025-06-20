N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
query = []
for i in range(Q):
    R, X = list(map(int, input().split()))
    query.append((i, R-1, X))

# stackとして使うのでRで逆順ソート
query.sort(key=lambda x: -x[1])

# print(*query, sep='\n')

ans = [None]*Q

dp = [float('inf') for _ in range(N+1)]
dp[0] = 0
for i in range(N):
    a = A[i]

    ok = 0
    ng = N+1
    while ng - ok > 1:
        test = (ng+ok)//2
        if dp[test] < a:
            ok = test
        else:
            ng = test
    
    if dp[ok+1] > a:
        dp[ok+1] = a
    
    # print(dp)

    while query and query[-1][1] == i:
        ans_idx, _, x = query.pop()

        ok = 0
        ng = N+1
        while ng - ok > 1:
            test = (ng+ok)//2
            if dp[test] <= x:
                ok = test
            else:
                ng = test
        
        ans[ans_idx] = ok
        # print(ans_idx, _, x, ok)

print(*ans, sep='\n')