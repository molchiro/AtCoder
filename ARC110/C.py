N = int(input())
P = list(map(int, input().split()))

d = [-1]*(N+1)
for i in range(N):
    d[P[i]] = i

f = [0]*(N+1)
ans = []
for i in range(1, N+1):
    while d[i] != i-1:
        now = d[i]
        if f[now-1] == 0:
            f[now-1] = 1
            l = P[now-1]
            P[now-1], P[now] = i, l
            d[l], d[i] = now, now-1
            ans.append(now)
        else:
            print(-1)
            exit()
if sum(f) == N-1:
    print(*ans, sep='\n')
else:
    print(-1)