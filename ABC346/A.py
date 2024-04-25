N = int(input())
A = list(map(int, input().split()))
ans = []
for i in range(N-1):
    ans.append(A[i]*A[i+1])
print(*ans)