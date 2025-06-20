from collections import defaultdict

T = int(input())

def solve(n, nums):
    dp = defaultdict(int)
    dp[0] = 0
    for num in nums:
        ndp = defaultdict(int)
        for k, v in dp.items():
            # (を選ぶ
            if k < n:
                ndp[k+1] = max(ndp[k+1], v+num)
            # )を選ぶ
            if k > 0:
                ndp[k-1] = max(ndp[k-1], v)

        dp = ndp
        # print(dp)

    return dp[0]

for _ in range(T):
    N = int(input())
    A = []
    for _ in range(2*N):
        A.append(int(input()))
    print(solve(N, A))