from heapq import heapify, heappop, heappush

# 定数倍高速化で頑張った解き方
R, C = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(R)]
B = [list(map(int, input().split())) for _ in range(R-1)]
dist = [[10**6]*C for _ in range(R)]
fixed = [[0]*C for _ in range(R)]
hq = [(0, 0, 0)] # (dist, r, c)
while hq:
    d, r, c = heappop(hq)
    if fixed[r][c]:
        continue
    dist[r][c] = d
    fixed[r][c] = 1
    if (r, c) == (R-1, C-1):
        print(dist[r][c])
        exit()
    if 0 < c:
        dd = A[r][c-1]
        if d + dd < dist[r][c-1]:
            dist[r][c-1] = d + dd
            heappush(hq, (d+dd, r, c-1))
    if c < C-1:
        dd = A[r][c]
        if d + dd < dist[r][c+1]:
            dist[r][c+1] = d + dd
            heappush(hq, (d+dd, r, c+1))
    if r < R-1:
        dd = B[r][c]
        if d + dd < dist[r+1][c]:
            dist[r+1][c] = d + dd
            heappush(hq, (d+dd, r+1, c))
    for i in range(1, r+1):
        dd = i+1
        if d + dd < dist[r-i][c]:
            dist[r-i][c] = d + dd
            heappush(hq, (d+dd, r-i, c))
        # ここの枝刈りがポイント
        elif d + dd > dist[r-i][c]:
            break