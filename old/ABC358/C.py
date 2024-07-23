N, M = list(map(int, input().split()))
S = []
for _ in range(N):
    s = input()
    S.append([0 if x == 'x' else 1 for x in s])

# print(S)

ans = N
for i in range(1<<N):
    p = [0]*M
    for j in range(N):
        if i >> j & 1:
            for k in range(M):
                if S[j][k] == 1:
                    p[k] += 1
    # print(i, p)

    f = 1
    for j in range(M):
        if p[j] == 0:
            f = 0
    
    if f:
        ans = min(ans, i.bit_count())

print(ans)