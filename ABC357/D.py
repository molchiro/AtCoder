from atcoder.modint import Modint, ModContext

N = int(input())
mod = 998244353
with ModContext(mod):
    a = Modint(N)
    b = Modint(pow(10, N*len(str(N)), mod))-1
    c = Modint(pow(10, len(str(N)), mod))-1

    print((a*b*c.inv()).val())