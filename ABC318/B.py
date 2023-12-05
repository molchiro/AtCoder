N = int(input())
field = [[0]*101 for _ in range(101)]
for _ in range(N):
    A, B, C, D = list(map(int, input().split()))
    for h in range(C, D):
        for w in range(A, B):
            field[h][w] = 1
ans = sum([sum(row) for row in field])
print(ans)
