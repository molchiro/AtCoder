from math import ceil

def check(A, K, L):
    i = 0
    for a in A:
        i += ceil(a/L)-1
        if i > K:
            return False
    return True

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort(reverse=True)
l = 0
r = A[0]
while l + 1 < r:
    m = (l+r)//2
    if check(A, K, m):
        r = m
    else:
        l = m
print(r)