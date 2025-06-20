A = list(map(int, input().split()))
from collections import Counter
A_C = Counter(A)
V = [v for k, v in A_C.items() if v >= 2]
# print(V)
V.sort()
if len(V) >= 2 and V[0] >= 2 and V[-1] >=3:
    print('Yes')
else:
    print('No')