N = int(input())
A = list(map(int, input().split()))

from collections import Counter

C = Counter(A)

ans = 0

for k, v in C.items():
    if v >= 2:
        ans += v*(v-1)//2 * (N-v)

print(ans)
