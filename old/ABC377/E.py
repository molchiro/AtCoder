N, K = list(map(int, input().split()))
P = list(map(lambda x: int(x) - 1, input().split()))

to = [None]*N
for i, p in enumerate(P):
    to[p] = i

doubling = [to[:]]

for _ in range(64):
    tmp = [None]*N
    for j, v in enumerate(doubling[-1]):
        tmp[j] = doubling[-1][v]
    doubling.append(tmp)

print(doubling)

ans = P
for i in range(64):
    if K >> i & 1:
        # print(i)
        nans = [None]*N
        for j, v in enumerate(ans):
           nans[doubling[i][j]] = v 
        ans = nans
        print(ans)
            

print(*[x+1 for x in ans])