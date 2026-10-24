N, M = list(map(int, input().split()))
S = input()



from functools import cache

mod = 998244353

@cache
def kaijo(n):
    if n == 1:
        return 1
    
    return n*kaijo(n-1)%mod

for i in range(1, 10**6):
    kaijo(i)

from atcoder.dsu import DSU
from atcoder.modint import Modint, ModContext

with ModContext(mod):
    dsu = DSU(N)
    f = 1

    for _ in range(M):
        A, B = list(map(lambda x: int(x) - 1, input().split()))
        dsu.merge(A, B)

    
    ans = Modint(1)
    for group in dsu.groups():
        tmp = ''
        accum = Modint(1)
        ct = [0]*26
        for idx in group:
            tmp += S[idx]
            ct[ord(S[idx])-ord('a')] += 1
        # print(tmp)
        # print(ct)
        
        accum *= Modint(kaijo(sum(ct)))
        for x in ct:
            if x == 0:
                continue
            if x > 1:
                f = 0
            accum *= Modint(kaijo(x)).inv()

        ans *= accum
        # print(ans.val())
    
    if f:
        print((ans*Modint(2).inv()).val())
    else:
        print(ans.val())
