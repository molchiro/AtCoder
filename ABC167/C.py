N, M, X = list(map(int, input().split()))
conditions = [str(bin((2**N + i) & (2**(N+1) - 1)))[3:] for i in range(2**N)]
Q = [list(map(int, input().split())) for i in range(N)]
ans = -1
for c in conditions:
    res = [0]*(M+1)
    for i in range(N):
        if c[i] == '1':
            for j in range(M+1):
                res[j] += Q[i][j]

    failed = False
    for i in range(1, M+1):
        if res[i] >= X:
            continue
        else:
            failed = True
    if failed:
        continue
    else:
        if ans == -1:
            ans = res[0]
        else:
            ans = min(ans, res[0])

print(ans)