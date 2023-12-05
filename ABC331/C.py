from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))
# Counterのほうがいいか
dd = defaultdict(int)
for a in A:
    dd[a] += 1

d = dict()
tmp = sum(A)
for key in sorted(dd.keys()):
    tmp -= dd[key]*key
    d[key] = tmp

print(*[d[x] for x in A])