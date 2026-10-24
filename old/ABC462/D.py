N, D = list(map(int, input().split()))

events = []
for _ in range(N):
    s, t = list(map(int, input().split()))
    events.append((s, 1))
    events.append((max(s,t-D+1), -1))
events.sort(reverse=True)
ans = 0
n = 0
for i in range(2*10**6):
    while events and events[-1][0] == i:
        _, k = events.pop()
        n += k
    ans += n*(n-1)//2
    # if n > 0:
    #     print(i, n)


print(ans)