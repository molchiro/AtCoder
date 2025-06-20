N = int(input())
A = list(map(int, input().split()))

from bisect import bisect_left, bisect_right

ans = 0
for a in A:
    idx = bisect_left(A, a*2)
    ans += N-idx
print(ans)
