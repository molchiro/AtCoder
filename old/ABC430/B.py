N, M = list(map(int, input().split()))
S = [input() for _ in range(N)]

s = set()

for h in range(N-M+1):
    for w in range(N-M+1):
        tmp = ''
        for i in range(M):
            for j in range(M):
                tmp += S[h+i][w+j]
        s.add(tmp)

print(len(s))