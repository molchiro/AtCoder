N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
for _ in range(N):
    X = list(map(int, input().split()))
    for j in range(M):
        A[j] -= X[j]

f = 1
for j in range(M):
    if A[j] > 0:
        f = 0

print('Yes' if f else 'No')