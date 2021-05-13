from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
A_cumsum = list(accumulate(A))
ans = 0
for i in range(N-1):
    S = (A_cumsum[-1]-A_cumsum[i])%(10**9+7)
    ans += A[i]*S
    ans %= 10**9+7
print(ans)