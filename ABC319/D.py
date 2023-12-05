N, M = list(map(int, input().split()))
L = list(map(int, input().split()))
max_l = max(L)
ng = 0
ok = sum(L)+len(L)
print(ng, ok)
while ok-ng >= 2:
    test = (ok+ng)//2
    print(test)
    input()

    if test < max_l:
        ng = test
        continue

    line_remainder = test
    i = 1
    for l in L:
        if line_remainder >= l:
            line_remainder -= l+1
        else:
            i += 1
            line_remainder = test
            line_remainder -= l+1
        if i > M:
            ng = test
            break
    else:
        ok = test

print(ok)
                
