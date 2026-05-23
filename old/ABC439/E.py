
import bisect
def LIS(seq):
    res = [seq[0]]
    for i in range(len(seq)):
        if seq[i] > res[-1]:
            res.append(seq[i])
        else:
            res[bisect.bisect_left(res, seq[i])] = seq[i]

    return res

N = int(input())
kites = [list(map(int, input().split())) for _ in range(N)]

from collections import defaultdict

dd = defaultdict(list)
for a, b in kites:
    dd[a].append(b)

array = []
for a in sorted(dd.keys()):
    for b in sorted(dd[a], reverse=True):
        array.append(b)

lis = LIS(array)
print(len(lis))