N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
i = 0
ans = sum([A[i] for i in range(N//2)])*2
if N%2 == 1:
    ans += A[N//2]
ans -= A[0]
print(ans)