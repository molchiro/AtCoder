import sys
sys.setrecursionlimit(10**9)

H, W, A, B = list(map(int, input().split()))
field = [[0]*W + [-1] for _ in range(H)] + [[-1]*(W+1)]
ans = [0]

def solve(i, j, A):
    # print(*field, sep='\n')
    if A == 0:
        ans[0] += 1
        return
    if i >= H:
        return
    if j >= W:
        solve(i+1, 0, A)
        return
    if field[i][j] != 0:
        # print(i, j)
        solve(i, j+1, A)
        return
    
    # 横に置く
    if field[i][j+1] == 0:
        field[i][j] = 1
        field[i][j+1] = 1
        solve(i, j+1, A-1)
        field[i][j+1] = 0
    # 縦に置く
    if field[i+1][j] == 0:
        field[i][j] = 1
        field[i+1][j] = 1
        solve(i, j+1, A-1)
        field[i+1][j] = 0
    # Bを置く
    field[i][j] = 2
    solve(i, j+1, A)
    field[i][j] = 0
    
solve(0, 0, A)

print(ans[0])