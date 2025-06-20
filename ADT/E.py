import sys
sys.setrecursionlimit(10**9)

N = int(input())

from functools import cache

@cache
def solve(x):
    if x == 1:
        return 0
    
    if x % 2:
        return x + solve(x//2) + solve(x - x//2)
    else:
        return x + solve(x//2) * 2

print(solve(N))