N, T = list(map(int, input().split()))
A = list(map(int, input().split()))

B = A[:N//2]
C = A[N//2:]

D = [0]
for b in B:
    tmp = []
    for d in D:
        if b+d < T:
            tmp.append(b+d)
    D += tmp

E = [0]
for c in C:
    tmp = []
    for e in E:
        if c+e <= T:
            tmp.append(c+e)
    E += tmp

D.sort()
E.sort()

ans = 0
r = len(E)-1
for d in D:
    while r >= 0 and E[r] + d > T:
        r -= 1
    ans = max(ans, d+E[r])

print(ans)