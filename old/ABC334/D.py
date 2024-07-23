N, Q = list(map(int, input().split()))
R = list(map(int, input().split()))
R.sort()
cumsum = [0]
for r in R:
    cumsum.append(cumsum[-1]+r)

from bisect import bisect_right

for _ in range(Q):
    q = int(input())
    print(bisect_right(cumsum, q)-1)