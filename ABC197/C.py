from itertools import product
N = int(input())
A = list(map(int, input().split()))
ans = float('inf')
for pattern in product([0, 1], repeat=N-1):
    # if pattern == tuple([0]*(N-1)):
    #     continue
    tmp = A[0]
    l = []
    for i, f in enumerate(pattern):
        if f:
            l.append(tmp)
            tmp = A[i+1]
        else:
            tmp |= A[i+1]
    l.append(tmp)
    tmp = 0
    for e in l:
        tmp ^= e
    ans = min(ans, tmp)
print(ans)    