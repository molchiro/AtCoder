N, T = list(map(int, input().split()))
A = list(map(lambda x: int(x) - 1, input().split()))

vert = [N]*N
hori = [N]*N
diag1 = {i*N + i for i in range(N)}
diag2 = {i*N + N - 1 - i for i in range(N)}

for i, a in enumerate(A):
    vert[a%N] -= 1
    hori[a//N] -= 1
    if a in diag1:
        diag1.remove(a)
    if a in diag2: 
        diag2.remove(a)

    if vert[a%N] == 0 or hori[a//N] == 0 or len(diag1) == 0 or len(diag2) == 0:
        print(i+1)
        break
else:
    print(-1)