from collections import deque

H, W = list(map(int, input().split()))
Ch, Cw = list(map(lambda x: int(x) - 1, input().split()))
Dh, Dw = list(map(lambda x: int(x) - 1, input().split()))
S = [input() for _ in range(H)]
maze = [[-1]*W for _ in range(H)]

def walk(h, w, warp_n):
    ans = []
    if maze[h][w] != -1:
        return []
    else:
        maze[h][w] = warp_n
        ans += [(h, w)]
        
    return ans

queue = deque([(Ch, Cw, 0)])
while queue:
    h, w, warp_n = queue.popleft()
    if maze[h][w] != -1:
        continue
    maze[h][w] = warp_n
    # walk
    for dh, dw in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if h+dh < 0 or w+dw < 0 or h+dh >= H or w+dw >= W:
                continue
            if S[h+dh][w+dw] == '#':
                continue
            queue.appendleft((h+dh, w+dw, warp_n))
    # warp
    for dh in range(-2, 3):
        for dw in range(-2, 3):
            if h+dh < 0 or w+dw < 0 or h+dh >= H or w+dw >= W:
                continue
            if S[h+dh][w+dw] == '#':
                continue
            if dh == 0 and dw == 0:
                continue
            queue.append((h+dh, w+dw, warp_n+1))

print(maze[Dh][Dw])