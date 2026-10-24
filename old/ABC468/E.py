from atcoder.modint import Modint, ModContext
from copy import deepcopy

mod = 998244353
with ModContext(mod):
    N = int(input())
    A = list(map(int, input().split()))

    accum = Modint(sum(A))
    B = [deepcopy(accum)]

    for i in range(N//2):
        accum -= Modint(A[i])+Modint(A[-1-i])
        B.append(B[-1] + deepcopy(accum))
    
    if N%2 == 0:
        B.pop()

    # print(*[x.val() for x in B])

    for i in range(N//2-1, -1, -1):
        B.append(B[-1] - deepcopy(accum))
        accum += Modint(A[i])+Modint(A[-1-i])
    
    # print(*[x.val() for x in B])

    ans = Modint()
    for i, b in enumerate(B):
        ans += b * Modint(i+1).inv()
    
    print(ans.val())