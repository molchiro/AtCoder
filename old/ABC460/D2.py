
H, W = list(map(int, input().split()))
ans = [[None]*W for _ in range(H)]

seen = set()
queue = []
for h in range(H):
    row = input()
    for w in range(W):
        if row[w] == '#':
            ans[h][w] = 1
            seen.add((h, w))
            queue.append((h, w))

# print(*ans, sep='\n')
# #しか周りにない場所は決まってないとみなす
stack = []
for h in range(H):
    for w in range(W):
        f = 1
        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
            nh = h+dh
            nw = w+dw
            if 0 <= nh < H and 0 <= nw < W:
                if ans[nh][nw] == None:
                    f = 0
        if f:
            stack.append((h, w))
for h, w in stack:
    ans[h][w] = None
# print(*ans, sep='\n')


while queue:
    next_queue = []
    for h, w in queue:
        for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
            nh = h+dh
            nw = w+dw
            if 0 <= nh < H and 0 <= nw < W:
                if (nh, nw) in seen:
                    continue
                ans[nh][nw] = (ans[h][w]+1)%2
                next_queue.append((nh, nw))
                seen.add((nh, nw))
    
    queue = next_queue
    # print(*ans, sep='\n')
    # print(next_queue)
    # input()

ans = [''.join(['#' if x else '.' for x in row]) for row in ans]
print(*ans, sep='\n')