N = int(input())
A = list(map(int, input().split()))
tmp = A[0]
ans = 0
for i in range(1, N):
    if A[i] < tmp:
        ans += tmp - A[i]
    else:
        tmp = A[i]
print(ans)