N = int(input())
A = list(map(int, input().split()))
if A[0] != 1 or A[-1] != N%2:
    print(0)
    exit()

A.append((N+1)%2)
prev = 1
accum = 0
l = []
for i, a in enumerate(A):
    if (i+1)%2 == a:
        if prev == 1:
            accum -= 1
            if accum > 0:
                if accum%2 == 0:
                    print(0)
                    exit()
                l.append(accum)
            accum = 0
        else:
            accum += 1
        prev = 1
    else:
        accum += 1
        prev = 0

print(l)
if len(l) == 0:
    print(0)
    exit()

m = [x//2+1 for x in l]
print(m)

from functools import cache

mod = 998244353

@cache
def kaijo(n):
    if n == 1:
        return 1
    
    return n*kaijo(n-1)%mod


from atcoder.modint import Modint, ModContext

mod = 998244353
with ModContext(mod):
    ans = Modint(1)
    accum = 0
    for x in m:
        ans *= Modint(kaijo(2*x))
        ans *= Modint(kaijo(x+1)).inv()
        ans *= Modint(kaijo(x)).inv()
        accum += x
    
    ans *= Modint(kaijo(accum))
    for x in m:
        ans *= Modint(kaijo(x)).inv()

    print(ans.val())