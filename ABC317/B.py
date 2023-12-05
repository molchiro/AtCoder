N = int(input())
A = list(map(int, input().split()))
A.sort()
offset = A[0]
for i in range(N):
    if A[i] != i+offset:
        print(i+offset)
        break