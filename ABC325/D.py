N = int(input())
events = [list(map(int, input().split())) for _ in range(N)]
events.sort()

from heapq import heapify, heappop, heappush

hq = []
heapify(hq)
t = 0
ans = 0
e_idx = 0
while hq or e_idx < N:
    if hq:
        t_out = heappop(hq)
        if t <= t_out:
            ans += 1
            t += 1
    else:
        T, D = events[e_idx]
        heappush(hq, T+D)
        e_idx += 1
        t = T
    while e_idx < N and events[e_idx][0] <= t:
        T, D = events[e_idx]
        heappush(hq, T+D)
        e_idx += 1
    # print(t, hq)
print(ans)