N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
accum = sum(A)
f = 0
for a in A:
    if accum-a == M:
        f = 1
print('Yes' if f else 'No')