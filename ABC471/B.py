N = int(input())

from collections import defaultdict

dd = defaultdict(int)

for _ in range(N):
    dd[input().lower()] += 1

print(max(dd.values()))