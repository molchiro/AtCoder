T = int(input())
for _ in range(T):
    a, b, c = list(map(int, input().split()))
    ok = 0
    ng = 10**18
    while ng - ok > 1:
        test = (ng+ok)//2
        if a-test >= 0 and c-test >= 0 and a-test + b + c-test >= test:
            ok = test
        else:
            ng = test
    print(ok)