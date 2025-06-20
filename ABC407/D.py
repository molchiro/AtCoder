import sys
sys.setrecursionlimit(10**9)

H, W = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(H)]
ans = 0

def dfs(board, n):
    global ans, A, H, W

    h = n//W
    w = n%W
    # print(h, w)
    # print(n, h, w)

    if n >= H*W:

        tmp = 0
        for x in range(H):
            for y in range(W):
                if board[x][y] == 0:
                    tmp ^= A[x][y]
        # print(tmp)
        # print(*board, sep='\n')
        ans = max(ans, tmp)
        return

    # おかない
    dfs(board, n+1)

    # 縦置き
    if board[h][w] == 0 and h < H-1 and board[h+1][w] == 0:

        board[h][w] = 1
        board[h+1][w] = 1
        dfs(board, n+1)
        board[h][w] = 0
        board[h+1][w] = 0

    # 横置き
    if board[h][w] == 0 and w < W-1 and board[h][w+1] == 0:
        board[h][w+1] = 1
        board[h][w] = 1
        dfs(board, n+1)
        board[h][w] = 0
        board[h][w+1] = 0

dfs([[0 for _ in range(W)] for _ in range(H)], 0)
print(ans)