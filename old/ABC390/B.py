N = int(input())
A = list(map(int, input().split()))
r = A[1]/A[0]
f = 1
for i in range(2, N):
    if A[i] != A[i-1]*r:
        f = 0

print('Yes' if f else 'No')