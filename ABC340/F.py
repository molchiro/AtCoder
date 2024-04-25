X, Y = list(map(int, input().split()))
if X == 0:
    if abs(Y) == 1:
        print(2, 0)
    elif abs(Y) == 2:
        print(1, 0)
    else:
        print(-1)
elif Y == 0:
    if abs(X) == 1:
        print(0, 2)
    elif abs(X) == 2:
        print(0, 1)
    else:
        print(-1)
else:
    
    def extgcd(a, b):
        if b:
            d, y, x = extgcd(b, a % b)
            y -= (a // b)*x
            return d, x, y
        return a, 1, 0
    
    # g, x, y = extgcd(Y, -X)
    # # print(g, x, y)
    # if abs(g) <= 2:
    #     print(x//g*2, y//g*2)
    # else:
    #     print(-1)

    from math import gcd

    g = gcd(abs(X), abs(Y))
    if g >= 3:
        print(-1)
    elif g == 2:
        X //= 2
        Y //= 2
        _, x, y = extgcd(Y, -X)
        print(x, y)
    else:
        _, x, y = extgcd(Y, -X)
        print(x*2, y*2)
