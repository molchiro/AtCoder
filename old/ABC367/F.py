N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

from collections import Counter

cumsum_A = [Counter()]
for a in A:
    cumsum_A.append(cumsum_A[-1]+Counter([a]))
cumsum_B = [Counter()]
for b in B:
    cumsum_B.append(cumsum_B[-1]+Counter([b]))

for _ in range(Q):
    l, r, L, R = list(map(lambda x: int(x) - 1, input().split()))
    if (cumsum_A[r+1]-cumsum_A[l]) == (cumsum_B[R+1]-cumsum_B[L]):
        print('Yes')
    else:
        print('No')