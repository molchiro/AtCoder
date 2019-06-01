N, M = list(map(int, input().split()))

Lmax = 0
Rmin = N
for i in range(M):
    L, R = list(map(int, input().split()))
    Lmax = max(Lmax, L)
    Rmin = min(Rmin, R)

print(max(Rmin - Lmax +1, 0))