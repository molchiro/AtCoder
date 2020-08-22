from collections import deque

H, W = list(map(int, input().split()))
Ch, Cw = list(map(lambda x: int(x) - 1, input().split()))
Dh, Dw = list(map(lambda x: int(x) - 1, input().split()))
S = [input() for _ in range(H)]

def walk(i, j):
    ans = []
    for h, w in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        # print(h, w)
        if h >= 0 and w >= 0 and h < H and w < W:
            # print('hoen')
            if S[h][w] == '.':
                if maze[h][w] == -1:
                    ans.append((h, w))
    return ans

def warp(i, j):
    tmp = []
    for dh in range(-2, 3):
        for dw in range(-2, 3):
            if not (dh == 0 and dw == 0):
                tmp.append([i + dh, j + dw])
    ans = []
    for h, w in tmp:
        if h >= 0 and w >= 0 and h < H and w < W:
            if S[h][w] == '.':
                if maze[h][w] == -1:
                    ans.append((h, w))
    return ans

maze = [[-1]*W for _ in range(H)]
warp_n = 0
maze[Ch][Cw] = 0
walk_stack= deque(walk(Ch, Cw))
warp_set = set(warp(Ch, Cw))
# print(walk(Ch, Cw))
# print(warp(Ch, Cw))
# print('-----')
while walk_stack or warp_set:
    while walk_stack:
        h, w = walk_stack.pop()
        if maze[h][w] == -1:
            maze[h][w] = warp_n
            walk_stack.extend(walk(h, w))
            warp_set |= set(warp(h, w))
    warp_n += 1
    # print(*maze, sep='\n')
    # print('-----')
    next_warp = set()
    for h, w in warp_set:
        if maze[h][w] == -1:
            maze[h][w] = warp_n
            walk_stack.extend(walk(h, w))
            next_warp |= set(warp(h, w))
    warp_set = next_warp
print(maze[Dh][Dw])