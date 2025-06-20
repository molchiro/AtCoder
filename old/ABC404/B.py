N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]

ans = float('inf')
for i in range(4):
    tmp = i
    for h in range(N):
        for w in range(N):
            if S[h][w] != T[h][w]:
                tmp += 1
    ans = min(ans, tmp)

    S = S[::-1]
    S = list(map(list, zip(*S)))

print(ans)