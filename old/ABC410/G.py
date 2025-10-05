N = int(input())
seq = []
for _ in range(N):
    A, B = list(map(int, input().split()))
    if A > B:
        A, B = B, A
    seq.append((A, B))
    seq.append((B, A+2*N))

import bisect
def LIS(seq):
    res = [seq[0]]
    for i in range(len(seq)):
        if seq[i] > res[-1]:
            res.append(seq[i])
        else:
            res[bisect.bisect_left(res, seq[i])] = seq[i]

    return res

lis = LIS([-l for l, _ in sorted(seq, key=lambda x: x[1])])
print(len(lis))
    