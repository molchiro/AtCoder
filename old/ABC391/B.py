N, M = list(map(int, input().split()))
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

for h in range(N-M+1):
    for w in range(N-M+1):
        f = 1
        for i in range(M):
            for j in range(M):
                if not S[h+i][w+j] == T[i][j]:
                    f = 0
        if f:
            print(h+1, w+1)
            exit()
