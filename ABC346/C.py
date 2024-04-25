N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
from bisect import bisect_right
ans = (K+1)*K//2 - sum(set(A[:bisect_right(A, K)]))
print(ans)