N = int(input())

for d in range(1, 10**6+1):
    ok = 1
    ng = 10**10
    while ng - ok > 1:
        x = (ng+ok)//2
        z = d**3 - 3*(d**2) * x + 3*d * (x**2)
        if z == N:
            print(x, x - d)
            exit()
        elif z < N :
            ok = x
        else:
            ng = x

print(-1)