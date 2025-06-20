N = int(input())

ans = 0
a = 2
while a <= N:
    ok = 1
    ng = 10**19
    while ng - ok > 1:
        test = (ng+ok)//2
        if a*test*test <= N:
            ok = test
        else:
            ng = test
    ans += ok - ok//2
    a *= 2
    # print(ans)
print(ans)