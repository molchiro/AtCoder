N = int(input())

C = list(map(int, input().split()))

from collections import Counter

counter = Counter(C)

print(N-max(counter.values()))