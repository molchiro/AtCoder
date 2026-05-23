N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict

dd = defaultdict(int)

for a in A:
    dd[a] = max(dd[a], dd[a-1]+1)

print(max(dd.values()))