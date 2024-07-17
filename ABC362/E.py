from collections import defaultdict

mod = 998244353

N = int(input())
A = list(map(int, input().split()))

dp = [defaultdict(int) for _ in range(N+1)]
for i in range(1, N):
    a = A[i]
    ndp = [defaultdict(int) for _ in range(N+1)]
    for k in range(N+1):
        for (d, prev), v in dp[k].items():
            ndp[k][(d, prev)] = v
    # 既存の数列
    for k in range(1, i+1):
        for (d, prev), v in dp[k].items():
            # print('check', d, prev, a)
            if a-prev == d:
                ndp[k+1][(d, a)] += v
                ndp[k+1][(d, a)] %= mod
            # print(ndp[k])
            # print(ndp[k+1])

    # 新しいペア
    for j in range(i):
        ndp[2][(A[i]-A[j], A[i])] += 1
        ndp[2][(A[i]-A[j], A[i])] %= mod
    
    dp = ndp
    # print(*dp, sep='\n')
    # input()

dp[1][(0, 0)] = N
# print(*dp, sep='\n')

ans = [0]*N
for i in range(N):
    for v in dp[i+1].values():
        ans[i] += v
        ans[i] %= mod

print(*ans)



