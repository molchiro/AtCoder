from math import sqrt

def f(x, y):
    return int(str(x)+str(y))

T = int(input())
for _ in range(T):
    C, D = list(map(int, input().split()))
    Cs = str(C)

    x = int(sqrt(f(C, C)))
    ans = 0
    limit = f(C, C+D)
    while x**2 <= limit:
        S = str(x**2)
        if S[:len(Cs)] == Cs:
            rs = S[len(Cs):]
            if rs and rs[0] != '0':
                r = int(rs)
                # print(l, r)
                if 0 <= r-C <= D:
                    # print('hit!', S, C, r)
                    ans += 1



        x += 1

    print(ans)