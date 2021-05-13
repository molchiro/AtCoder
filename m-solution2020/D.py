N = int(input())
A = list(map(int, input().split()))
cash = 1000
for i in range(N-1):
    if A[i] < A[i+1]:
        cash += (A[i+1]-A[i])*(cash//A[i])
print(cash)