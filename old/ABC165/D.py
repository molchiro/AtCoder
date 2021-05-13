def floor(A, B, x):
    return A*x//B - A*(x//B)

A, B, N = list(map(int, input().split()))
C = max(0, B*(N//B) - 1)
print(max(floor(A, B, N), floor(A, B, C)))