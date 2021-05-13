N = int(input())
A = [[0 for _ in range(9)] for _ in range(9)]
for i in range(1, N+1):
    S = str(i)
    if S[-1] == '0':
        continue
    A[int(S[0])-1][int(S[-1])-1] += 1
ans = 0
for i in range(9):
    for j in range(9):
        ans += A[i][j]*A[j][i]
print(ans)