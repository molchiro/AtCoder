N = int(input())
from collections import defaultdict
dd = defaultdict(int)

inf = 10**10

for _ in range(N):
    A, C = list(map(int, input().split()))
    dd[C] = min(dd[C], -inf+A)
# print(dd.values)
print(max(dd.values())+inf)