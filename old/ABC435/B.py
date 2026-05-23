N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(i, N):
        total = sum(A[i:j+1])
        f = 1
        for Ai in A[i:j+1]:
            if total%Ai == 0:
                f = 0
        ans += f
print(ans)