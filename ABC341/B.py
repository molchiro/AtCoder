N = int(input())
A = list(map(int, input().split()))
for i in range(N-1):
    S, T = list(map(int, input().split()))
    A[i+1] += T*(A[i]//S)

print(A[-1])