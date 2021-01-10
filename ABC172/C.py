from itertools import accumulate
from bisect import bisect

N, M, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_ = list(accumulate(A))
B_ = list(accumulate(B))
A_all = bisect(A_, K)
B_all = bisect(B_, K)
if B_all > A_all:
    A_, B_ = B_, A_
A_all, B_all = B_all, A_all
ans = 0
for i in range(A_all):
    ans = max(ans, i+1 + bisect(B_, K - A_[i]))
print(ans)