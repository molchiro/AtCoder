N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]
base = min([C[i][0] for i in range(N)])
A = [C[i][0] - base for i in range(N)]
B = [x - A[0] for x in C[0]]
for i in range(N):
    if [C[i][j] - A[i] for j in range(N)] != B:
        print('No')
        exit()
print('Yes')
print(*A)
print(*B)

list(map(lambda x: int(x) - 1, input().split()))