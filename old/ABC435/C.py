N = int(input())
A = list(map(int, input().split()))

pow = A[0]+1
ans = 1
for i in range(1, N):
    if pow <= i+1:
        break
    ans += 1
    pow = max(pow, A[i]+i+1)
print(ans)