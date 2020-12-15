from collections import deque

H, W = list(map(int, input().split()))
r, c = list(map(lambda x: int(x) - 1, input().split()))
field = [input() for _ in range(H)]

seen = [[0]*W for _ in range(H)]
q = deque()
q.append([r, c])
while q:
    h, w = q.popleft()
    if seen[h][w]:
        continue
    seen[h][w] = 1
    if h+1 < H and field[h+1][w] in ['.', '^']:
        q.append([h+1, w])
    if h-1 >= 0 and field[h-1][w] in ['.', 'v']:
        q.append([h-1, w])
    if w+1 < W and field[h][w+1] in ['.', '<']:
        q.append([h, w+1])
    if w-1 >= 0 and field[h][w-1] in ['.', '>']:
        q.append([h, w-1])

for h in range(H):
    for w in range(W):
        if field[h][w] == '#':
            print('#', end='')
        elif seen[h][w]:
            print('o', end='')
        else:
            print('x', end='')
    print()