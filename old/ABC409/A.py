N = int(input())
T = input()
A = input()
ans = 0
for i in range(N):
    if T[i] == A[i] == 'o':
        ans = 1
print('Yes' if ans else 'No')