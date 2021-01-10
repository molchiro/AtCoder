N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
inner = 0
for i in range(N):
    inner += A[i]*B[i]
print('Yes' if inner == 0 else 'No')