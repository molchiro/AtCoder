H, W = list(map(int, input().split()))

S = [list(input()) for _ in range(H)]

from collections import deque

dq = deque()

for h in range(H):
    for w in range(W):
        if S[h][w] == 'E':
            dq.append((h, w))

while dq:
    h, w = dq.popleft()

    for k, (dh, dw) in {'v': (-1, 0), '^': (1, 0), '<': (0, 1), '>': (0, -1)}.items():
        if not (0 <= h+dh < H):
            continue
        if not (0 <= w+dw < W):
            continue

        if not S[h+dh][w+dw] == '.':
            continue

        S[h+dh][w+dw] = k
        dq.append((h+dh, w+dw))

for h in range(H):
    print(''.join(S[h]))
