from math import gcd

N = int(input())
X = list(map(int, input().split()))
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
from itertools import product

ans = float('inf')
for pattern in product([0, 1], repeat=len(primes)):
    tmp = 1
    for i, f in enumerate(pattern):
        if f:
            tmp *= primes[i]
    satisfied = True
    for x in X:
        if gcd(x, tmp) == 1:
            satisfied = False
            break
    if satisfied:
        ans = min(ans, tmp)
print(ans)