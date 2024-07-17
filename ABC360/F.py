N = int(input())
lines = []
for i in range(N):
    L, R = list(map(int, input().split()))
    lines.append((L, R, i))
lines.sort()
events = []
for L, R, i in lines:
    events.append((L+1, +1, i))
    events.append((R, -1, i))

events2 = []
s = set()
k = 0
for x, y, i in events:
    if y == 1:
        s.add(i)
    else:
        s.remove(i)
    k += y
    events2.append((x, k, min(s)))

events3 = sorted(events2, key=lambda x: (x[1], x[0]))
e_n = len(events3)
idx = 0
ans = (10**10, 10**10, 0)
for x, k, l in events2:
    