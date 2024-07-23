N = int(input())
field = [['T']*(N+2)] + [['T']+ [0]*N + ['T'] for _ in range(N)] + [['T']*(N+2)]

d_idx = 0
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
now = (1, 1)
for i in range(N*N-1):
    r, c = now
    field[r][c] = i+1
    if field[r+d[d_idx][0]][c+d[d_idx][1]] != 0:
        d_idx += 1
        d_idx %= 4
    now = (r+d[d_idx][0], c+d[d_idx][1])
field[now[0]][now[1]] = 'T'

for r in range(N):
    print(*field[r+1][1:1+N])
    
