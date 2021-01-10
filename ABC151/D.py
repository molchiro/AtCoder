def solve(maze,H, W, S):
    next_set = set()
    next_set.add(S)
    seen = [[False]*W for _ in range(H)]
    n = 0
    while next_set:
        n += 1
        curr_ = list(next_set)
        next_set = set()
        for h, w in curr_:
            if seen[h][w]:
                continue
            seen[h][w] = True
            for nh, nw in maze[h][w]:
                if seen[nh][nw] == False:
                    next_set.add((nh, nw))
    return n-1

# 入力
H, W = list(map(int, input().split()))
maze = [[[] for _ in range(W)] for _ in range(H)]
for h in range(H):
    row = input()
    for w in range(W):
        if row[w] == '#':
            maze[h][w] = False


# mazeに移動可能移動可能なマスを記録
for h in range(H):
    for w in range(W):
        if maze[h][w] == False:
            continue
        for nh, nw in [(h+1, w), (h, w+1), (h-1, w), (h, w-1)]:
            if 0 <= nh < H and 0<= nw < W:
                if maze[nh][nw] != False:
                    maze[h][w].append((nh, nw))

ans = 0
for i in range(H*W-1):
        h = i//W
        w = i%W
        if maze[h][w]:
            ans = max(ans, solve(maze, H, W, (h, w)))

print(ans)
