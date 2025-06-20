N = int(input())
A = list(map(int, input().split()))

from collections import Counter

left_C = Counter()
right_C = Counter(A)

left_n = 0
right_n = len(right_C.keys())
ans = 0
for i in range(N-1):
    a = A[i]

    if left_C[a] == 0:
        left_n += 1
    left_C[a] += 1

    if right_C[a] == 1:
        right_n -= 1
    right_C[a] -= 1

    ans = max(ans, left_n + right_n)

print(ans)