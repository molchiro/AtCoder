A = [list(map(int, input().split())) for _ in range(3)]
board = [[-1]*3 for _ in range(3)]
# board: -1: undef, 0: aoki, 1: takahashi
# 相手が負ける手があるか
def solve(turn=1):
    global A, board
    teban = turn%2 # 1ならtakahash, 0ならaoki
    # 終了条件
    # 条件1
    hori = board
    vert = [[board[0][i], board[1][i], board[2][i]]for i in range(3)]
    diag = [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]
    if [teban]*3 in hori+vert+diag:
        return True
    # 条件2
    if turn == 10:
        score = {0: 0, 1: 0}
        for i in range(3):
            for j in range(3):
                score[board[i][j]] += A[i][j]
        return score[teban] > score[(teban+1)%2]

    # 必勝の手があれば勝ち
    for i in range(3):
        for j in range(3):
            if board[i][j] == -1:
                board[i][j] = teban
                res = solve(turn+1)
                board[i][j] = -1
                if not res:
                    return True
                
    # なければ負け
    return False

print('Takahashi' if not solve() else 'Aoki')