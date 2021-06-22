N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
K = [int(input()) for _ in range(Q)]

A.sort()
A.append(float('inf'))
ans = {}
now = 1
skipped = 0
for k in sorted(K):
    while k+skipped >= A[skipped]:
        now = A[skipped] + skipped + 1
        skipped += 1
    now = k + skipped
    ans[k] = now

for k in K:
    print(ans[k])