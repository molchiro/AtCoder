N = int(input())
A = [0, 0] + list(map(int, input().split()))
ans = 0
for i in range(2*N):
    # print(A[i], A[i+2])
    if A[i] == A[i+2]:
        ans += 1
print(ans)