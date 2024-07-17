N = int(input())
A = list(map(int, input().split()))
A.sort()
cumsum = [0]
for a in A:
    cumsum.append(cumsum[-1]+a)
ans = 0
from bisect import bisect_left
for i in range(N-1):
    idx = max(i+1, bisect_left(A, 10**8-A[i]))
    ans += A[i]*(N-i-1) + cumsum[-1]-cumsum[i+1] - (10**8)*(N-idx)
print(ans)