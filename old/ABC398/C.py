N = int(input())
A = list(map(int, input().split()))
# A = list(map(tuple, enumerate(map(int, input().split()))))
# print(A)
# A.sort(key=lambda x: x[1])
# print(A)

idxs = dict()
for i, a in enumerate(A):
    idxs[a] = i

from collections import Counter
C = Counter(A)
uniques = []
for k, v in C.items():
    if v == 1:
        uniques.append(k)
uniques.sort()

if len(uniques) == 0:
    print(-1)
else:
    print(idxs[uniques[-1]]+1)