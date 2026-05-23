N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

from collections import Counter

C = Counter(A)

B = [k*v for k, v in C.items()]

B.sort()

for _ in range(K):
    B.pop()
    if not B:
        break

print(sum(B))