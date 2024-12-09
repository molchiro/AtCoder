N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()

from bisect import bisect_left, bisect_right

cumsum = [0]
for a in A:
    cumsum.append(cumsum[-1]+a)

if sum(A) <= M:
    print('infinite')
else:
    ok = 0
    ng = 10**18
    while ng - ok > 1:
        test = (ng+ok)//2
        idx = bisect_right(A, test)

        if (N-idx)*test + cumsum[idx] <= M:
            ok = test
        else:
            ng = test
    print(ok)