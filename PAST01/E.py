N, Q = list(map(int, input().split()))
ff = [['N']*N for _ in range(N)]

for _ in range(Q):
    S = input().split()
    if S[0] == '1':
        ff[int(S[1])-1][int(S[2])-1] = 'Y'
    elif S[0] == '2':
        a = int(S[1]) - 1
        for i in range(N):
            if ff[i][a] == 'Y':
                ff[a][i] = 'Y'
    else:
        a = int(S[1]) - 1
        target = [0]*N
        for i in range(N):
            if ff[a][i] == 'Y':
                for j in range(N):
                    if ff[i][j] == 'Y':
                        target[j] = 1
        target[a] = 0
        for i in range(N):
            if target[i]:
                ff[a][i] = 'Y'

for i in range(N):
    print(''.join(ff[i]))