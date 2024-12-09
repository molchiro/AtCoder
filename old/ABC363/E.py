# 候補をヒープキューで管理
# 候補に入れたかどうかをseenで管理

H, W, Y = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(H)]
seen = [[0]*(W) for _ in range(H)]

from heapq import heapify, heappop, heappush

hq = []

def controller(h, w):
    global A
    global seen, hq

    if seen[h][w]:
        return
    
    heappush(hq, (A[h][w], (h, w)))
    seen[h][w] = 1

for h in range(H):
    for w in range(W):
        if h == 0 or h == H-1 or w == 0 or w == W-1:
            controller(h, w)

ans = H*W
for y in range(Y):
    while hq and hq[0][0] <= y+1:
        _, (h, w) = heappop(hq)
        ans -= 1
        for dh, dw in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if 0 <= h+dh < H and 0 <= w+dw < W:
                controller(h+dh, w+dw)

    print(ans)