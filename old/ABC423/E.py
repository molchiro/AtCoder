import sys

sys.setrecursionlimit(10**9)

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
cumsum = [0]
for a in A:
    cumsum.append(cumsum[-1]+a)

from functools import cache

@cache
def solve(l, r):
    global N, Q, A, cumsum
    if l > r:
        return 0
    return (cumsum[r] - cumsum[l-1])*(r-l+1) + solve(l+1, r-1)

for _ in range(Q):
    L, R = list(map(int, input().split()))
    print(solve(L, R))