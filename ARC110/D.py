from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

nCk = defaultdict(int)

def solve(n, k):
    if n < k:
        return 0
    if k == 0:
        return 1
    if nCk[(n, k)] == 0:
        tmp = solve(n-1, k-1) + solve(n-1, k)
        tmp %= 10**9+7
        nCk[(n, k)] = tmp
    return nCk[(n, k)]

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
S = sum(A)
print(solve(M+N, S+N))