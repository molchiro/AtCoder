N = int(input())
field = [[None]*N for _ in range(N)]
field[0][(N-1)//2] = 1
prev = (1, 0, (N-1)//2)

for _ in range(N*N-1):
    k, r, c = prev

    if field[(r-1)%N][(c+1)%N] == None:
        field[(r-1)%N][(c+1)%N] = k+1
        prev = (k+1, (r-1)%N, (c+1)%N)
    else:
        field[(r+1)%N][c] = k+1
        prev = (k+1, (r+1)%N, c)

for row in field:
    print(*row)