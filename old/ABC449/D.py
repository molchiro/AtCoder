
# [1, h], [1, w]の領域を求める
def culc1(h, w):
    if h < w:
        h, w = w, h

    if w == 0:
        return 0 
    
    a = 3
    l = (max(h, w)//2)*4 - 1
    n = h//2
    base = (a + l) * n // 2
    # print('base', base)
    if h == w:
        return base
    else:
        return base - culc2(w, h, h)

# (h1, h2], [1, W]の領域を求める
def culc2(h1, h2, w):
    # print(h1, h2, w)
    if w%2:
        w -= 1
    
    res = (w+1)*((h2-h1+1)//2)
    # print('res', res)
    if h1%2 == 1:
        res -= (h2+1-h1)//2

    # print('culc2', res)
    return res

# culc1の始まりが1よりでかいバージョン
def culc3(h1, h2, w1, w2):
    res = culc1(h2, w2)
    # print('debug',res)
    res -= culc1(h1-1, w2)
    # print('debug',res)
    res -= culc1(h2, w1-1)
    # print('debug',res)
    res += culc1(h1-1, w1-1)
    # print('debug',res)
    return res

assert culc2(3, 4, 4) == 4
assert culc2(1, 4, 4) == 8
assert culc2(2, 4, 4) == 5


assert culc1(3, 3) == 3
assert culc1(3, 4) == 6
assert culc1(1, 4) == 2
assert culc1(2, 1) == 1

assert culc3(2, 4, 1, 4) == 8
assert culc3(2, 4, 2, 4) == 6
assert culc3(3, 4, 2, 4) == 4

# wを負に拡張
def culc4(h1, h2, w1, w2):
    if w1 > 0:
        return culc3(h1, h2, w1, w2)
    elif w1 == 0:
        return culc3(h1, h2, 1, w2) + h2//2 - (h1-1)//2
    else:
        r = culc3(h1, h2, 1, w2)
        l = culc3(h1, h2, 1, -w1)
        return l + r + h2//2 - (h1-1)//2

assert culc4(1, 3, -4, 3) == 10
assert culc4(2, 3, -4, 3) == 7
assert culc4(2, 3, -4, -3) == 2
assert culc4(1, 1, -4, 3) == 3
assert culc4(2, 2, -4, 3) == 6
assert culc4(3, 3, -4, 3) == 1
assert culc4(4, 4, -4, 3) == 8
    
# hを負に拡張
def culc5(h1, h2, w1, w2):
    if h1 > 0:
        return culc4(h1, h2, w1, w2)
    elif h1 == 0:
        jiku = 0
        jiku += w2//2
        jiku -= w1//2
        if w1 <= 0 <= w2 or w1 == 0 or w2 == 0:
            jiku += 1
        # print (h1, w1, w2, jiku)
        return culc4(1, h2, w1, w2) + jiku
    else:
        u = culc4(1, h2, w1, w2)
        d = culc4(1, -h1, w1, w2)
        jiku = 0
        jiku += w2//2
        jiku -= w1//2
        if w1 <= 0 <= w2 or w1 == 0 or w2 == 0:
            jiku += 1
        return u + d + jiku

assert culc5(1, 3, -4, 3) == 10
assert culc5(0, 3, -4, 3) == 14
assert culc5(-1, 3, -4, 3) == 17
print( culc5(-2, 3, -4, 3))
assert culc5(-2, 3, -4, 3) == 23

L, R, D, U = list(map(int, input().split()))
print(culc5(D, U, L, R))