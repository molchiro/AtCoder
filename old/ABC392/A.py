A = list(map(int, input().split()))
print('Yes' if A[0]*A[1] == A[2] or A[0]*A[2] == A[1] or A[1]*A[2] == A[0] else 'No')