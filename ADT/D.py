N = list(map(int, input().split()))
T = input()
now = (0, 0)
direction = 0
d = [(1, 0), (0, -1),(-1, 0) ,(0, 1)]
for t in T:
    if t == 'R':
        direction += 1
        direction %= 4
    else:
        now = (now[0]+d[direction][0], now[1]+d[direction][1])

print(*now)
