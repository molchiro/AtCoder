from atcoder.modint import Modint, ModContext

N, C = list(map(int, input().split()))
A = list(map(int, input().split()))
A[C-1] += 1
C_A = A[C-1]
A.sort(reverse=True)


mod = 998244353
with ModContext(mod):

    total = Modint(sum(A)-1)
    cumsum_left = Modint(-1)
    cumsum_right = Modint(0)

    for i in range(N):
        cumsum_left += Modint(A[i])
        e = (total + cumsum_right) * cumsum_left.inv()
        cumsum_right += Modint(A[i]) * e

        if A[i] == C_A:
            print(e.val())
            break
    