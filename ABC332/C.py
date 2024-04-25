N, M = list(map(int, input().split()))
L = 0
m = M
l = L
for s in input():
    if s == '0':
        m = M
        l = L
    elif s == '1':
        if m > 0:
            m -= 1
        else:
            if l:
                l -= 1
            else:
                L += 1
    else:
        if l:
            l -= 1
        else:
            L += 1
print(L)