N = int(input())
P = list(map(int, input().split()))

d = {i+1: -1 for i in range(N)}
for i in range(N):
    d[P[i]] = i

f = [0]*(N+1)
ans = []
n = 0
for i in range(1, N+1):
    # print('t='+str(i))
    while d[i] != i-1:
        now = d[i]
        if f[now-1] == 0:
            n += 1
            f[now-1] = 1
            l = P[now-1]
            P[now-1], P[now] = i, l
            d[l] = now
            d[i] = now-1 
            ans.append(now)
        else:
            print(-1)
            exit()
    # print(P)
if n == N-1:
    print(*ans, sep='\n')
else:
    print(-1)