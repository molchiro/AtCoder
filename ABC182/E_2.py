import sys
input = sys.stdin.buffer.readline

H, W, N, M = list(map(int, input().split()))
# -1:block 0:default 1:lightened 2: light
grid = [[0]*W for _ in range(H)]
for _ in range(N):
    A, B = list(map(int, input().split()))
    grid[A-1][B-1] = 2
for _ in range(M):
    C, D = list(map(int, input().split()))
    grid[C-1][D-1] = -1

for _ in range(4):
    for h in range(len(grid)):
        is_beamed = 0
        for w in range(len(grid[0])):
            cell = grid[h][w]
            if cell == -1:
                is_beamed = 0
            elif cell == 2:
                is_beamed = 1
            elif cell == 0 and is_beamed:
                grid[h][w] = 1

    grid = grid[::-1]
    grid = list(map(list, zip(*grid)))

ans = 0
for h in range(H):
    for w in range(W):
        if grid[h][w] in [1, 2]:
            ans += 1

print(ans)