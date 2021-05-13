N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

A_pre = [-1]*N
ans = N
for i, a in enumerate(A):
    if i - A_pre[a] > M:
        ans = min(ans, a)
    A_pre[a] = i
for i in range(N):
    if N - A_pre[i] > M:
        ans = min(ans, i)

print(ans)