N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

l = 0
r = max(A)
while l + 1 < r:
    m = (l+r)//2
    n = sum([(x-1)//m for x in A])
    if n > K:
        l = m
    else:
        r = m
print(r)