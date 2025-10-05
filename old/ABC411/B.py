N = int(input())
D = list(map(int, input().split()))
ans = []
for i in range(N-1):
    tmp = []
    s = D[i]
    d = 0
    for j in range(i, N-1):
        d += D[j]
        tmp.append(d)
    print(*tmp)
