N = int(input())

row = [0]*N
col = [0]*N
field = [input() for _ in range(N)]
for r in range(N):
    for c in range(N):
        if field[r][c] == 'o':
            row[r] += 1
            col[c] += 1

ans = 0
for c in range(N):
    for r in range(N):
        if field[r][c] == 'o':
           ans += (row[r]-1)*(col[c]-1)

print(ans)