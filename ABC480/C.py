from heapq import heapify, heappop, heappush

N, K, T = list(map(int, input().split()))
A = list(map(int, input().split()))
hq = []
for a in A:
    heappush(hq, ((a, 1)))
    heappush(hq, ((a+K, -1)))

heappush(hq, (10**18, 0))

tmp = 0
ans = 0
heappush(hq, (0, 0))
while hq:
    t, v = heappop(hq)
    if t > T:
        break
    tmp += v
    while hq and hq[0][0] == t:
        _, vv = heappop(hq)
        tmp += vv

    if tmp == 0:
        d = min(T, hq[0][0]) - t
        # print(t, d)
        if d%K == 0:
            ans += d//K
        else:
            ans += d//K
            t += K*(d//K)
            ans += 1
            tmp += 1
            heappush(hq, (t+K, -1))
            # print('!', t)

    # print(t)


print(ans)
