N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

idx = M-1
day = N
ans = [0]*N
for i in range(N):
    if idx >= 0:
        if A[idx-1] == N-i:
            day = A[idx-1]
            idx -= 1
    ans[N-1-i] = (day-1)-(N-1-i)
print(*ans, sep='\n')