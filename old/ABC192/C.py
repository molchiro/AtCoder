def g1(x):
    Sx = list(str(x))
    Sx.sort(reverse=True)
    return int(''.join(Sx))

def g2(x):
    Sx = list(str(x))
    Sx.sort()
    return int(''.join(Sx))

def f(x):
    return g1(x)-g2(x)

N, K = list(map(int, input().split()))

ans = N
for i in range(K):
    ans = f(ans)

print(ans)