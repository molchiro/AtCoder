def isEternal(s, t):
    import fractions
    if len(s) < len(t):
        x = s[:]
        y = t[:]
    else:
        x = t[:]
        y = s[:]
    len_x = len(x)
    len_y = len(y)

    gcd = len_x * len_y // fractions.gcd(len_x, len_y)
    y_ = y * (gcd//len_y)

    top = y_.find(x)
    if top == -1:
        return False
    y__ = y_[top:] + y_[0:top]
    if y__ == x * (gcd//len_x):
        return True
    return False

s = input()
t = input()

cnt = -1
i = 0
if not isEternal(s, t):
    while True:
        tn = t * i
        while len(s) < len(tn) * 2:
            s = s + s
        if tn in s:
            cnt += 1
            i += 1 
        else:
            break
print(cnt)
