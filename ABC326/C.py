N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A.append(float('inf'))
A.sort()
r = 0
ans = 0
for i in range(N):
    while A[r] < A[i]+M:
        r += 1
    # print(i, r)
    ans = max(ans, r-i)
print(ans)