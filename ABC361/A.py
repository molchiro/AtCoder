N, K, X = list(map(int, input().split()))
A = list(map(int, input().split()))
B = A[:K] + [X] + A[K:]
print(*B)