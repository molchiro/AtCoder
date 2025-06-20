from functools import cache
import sys
sys.setrecursionlimit(10**9)

def added(tpl, value):
    return tuple(sorted(list(tpl) + [value]))

def removed(tpl, value):
    lst = list(tpl)
    lst.remove(value)
    return tuple(lst)

@cache
def solve(a, b, c):

    # print(a, b, c)

    for x in a:
        a_ = removed(a, x)
        c_ = added(c, x)
        res = solve(b, a_, c_)
        if not res:
            return 1
        for y in c:
            if y < x:
                res = solve(b, added(a_, y), removed(c_, y))
                if not res:
                    return 1

    return 0

N, M, L = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A = tuple(sorted(A))
B = tuple(sorted(B))
C = tuple(sorted(C))

print('Takahashi' if solve(A, B, C) else 'Aoki')