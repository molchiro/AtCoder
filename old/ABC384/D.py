N, S = list(map(int, input().split()))
A = list(map(int, input().split()))
cumsum = [0]
for a in A:
    cumsum.append(cumsum[-1]+a)

total = cumsum[-1]
S %= total

from bisect import bisect_left, bisect_right

accum = 0
A.append(0)
for i in range(N, -1, -1):
    accum += A[i]
    idx = bisect_left(cumsum, S-accum)
    if idx < N+1 and cumsum[idx] == S-accum:
        print('Yes')
        break
    
    idx = bisect_left(cumsum, S+total-accum)
    if idx < N+1 and cumsum[idx] == S+total-accum:
        print('Yes')
        break

else:
    print('No')
