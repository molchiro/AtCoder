X, Y, R = list(map(float, input().split()))
X -= int(X)
Y -= int(Y)

ans = 0
for y in range(int(Y-R), int(Y+R)+1):
    ans += 1
    Z = R**2 - (Y-y)**2
    l = int(X-R)-1
    r = int(X)
    while r - l > 1:
        m = (l+r)//2
        if (X-m)**2 <= Z:
            r = m
        else:
            l = m
    ans += int(X)-r

    l = int(X)
    r = int(X+R)+1
    while r - l > 1:
        m = (l+r)//2
        if (X-m)**2 <= Z:
            l = m
        else:
            r = m
    ans += l - int(X)
    # print(y, ans)
print(ans)