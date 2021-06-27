from math import ceil
A, B, C, D = list(map(int, input().split()))
if D*C-B > 0:
    print(ceil(A/(D*C-B)))
else:
    print(-1)