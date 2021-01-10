N, M = list(map(int, input().split()))
WA = [0]*N
AC = [False]*N
for _ in range(M):
    p, S = input().split()
    p = int(p)-1
    if S == 'WA':
        if AC[p] == False:
            WA[p] += 1
    else:
        AC[p] = True

ans = [0, 0]
for i in range(N):
    if AC[i] == False:
        continue
    ans[0] += 1
    ans[1] += WA[i]

print(*ans)