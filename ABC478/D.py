N, Q = list(map(int, input().split()))
events = []
for _ in range(Q):
    L, R, X = list(map(int, input().split()))
    events.append((L-1, 1, X))
    events.append((R, -1, X))

events.sort(key=lambda x: -x[0])
# print(events)
pool = [0]*200001
n = 0
ans = []
for i in range(N):
    while events and events[-1][0] == i:
        _, d, x = events.pop()
        if d > 0:
            if pool[x] == 0:
                n += 1
            pool[x] += 1
        else:
            if pool[x] == 1:
                n -= 1
            pool[x] -= 1
    ans.append(n)
    # print(pool[:50])
print(*ans)