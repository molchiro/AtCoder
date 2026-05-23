H, W = list(map(int, input().split()))
raw_field = []
field = [[-1]*(W+2)] + [[-1]+ [10**18]*W + [-1] for _ in range(H)] + [[-1]*(W+2)]
warp_list = [[] for _ in range(26)]
for h in range(H):
    row = input()
    raw_field.append(row)
    for w in range(W):
        s = row[w]
        if s == '.':
            continue
        elif s == '#':
            field[h+1][w+1] = -1
        else:
            x = ord(s) - ord('a')
            warp_list[x].append((h+1, w+1))

from collections import deque

dq = deque([(1, 1)])
field[1][1] = 0
f = 0
while dq:
    h, w = dq.popleft()
    d = field[h][w]
    if (h, w) == (H, W):
        f = 1
        break

    # walk
    for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nh, nw = h+dh, w+dw
        if field[nh][nw] != 10**18:
            continue
        field[nh][nw] = d+1
        dq.append((nh, nw))
    # warp
    if not raw_field[h-1][w-1] in ['.', '#']:
        x = ord(raw_field[h-1][w-1]) - ord('a')
        for nh, nw in warp_list[x]:
            if field[nh][nw] != 10**18:
                continue
            field[nh][nw] = d+1
            dq.append((nh, nw))
        warp_list[x] = []

if f:
    print(field[H][W])
else:
    print(-1)