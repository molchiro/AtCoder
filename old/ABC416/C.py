N, K, X = list(map(int, input().split()))
S = [input() for _ in range(N)]

from itertools import product

SS = []
for pattern in product(S, repeat=K):
    SS.append(''.join(pattern))
SS.sort()
# print(SS)
print(SS[X-1])
