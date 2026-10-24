N, M = list(map(int, input().split()))
S = [input() for _ in range(N)]
ans = [0]*N

for _ in range(M):
    T = input()
    wrongs = []
    for s in S:
        if len(s) == len(T):
            tmp = 0
            for i in range(len(T)):
                if s[i] != T[i]:
                    tmp += 1
            wrongs.append(tmp)
        else:
            wrongs.append(10**18)

    if 0 in wrongs:
        ans[wrongs.index(0)] += 1
    else:
        ct = 0
        for w in wrongs:
            if w == 1:
                ct += 1
        if ct == 1:
            ans[wrongs.index(1)] += 1

print(*ans, sep='\n')