from collections import deque

N, C = list(map(int, input().split()))
queue = []
for _ in range(N):
    a, b, c = list(map(int, input().split()))
    queue.append((a, c))
    queue.append((b+1, -c))
queue.sort(key=lambda x: x[0])

dq = deque(queue)

prev_day = 0
ans = 0
total_cost = 0
while dq:
    day = dq[0][0]
    c_diff = 0
    while dq and dq[0][0] == day:
        d, c = dq.popleft()
        c_diff += c
    if total_cost > C:
        ans += C*(day-prev_day)
    else:
        ans += total_cost*(day-prev_day)
    prev_day = day
    total_cost += c_diff

print(ans)