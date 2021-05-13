from itertools import combinations

def gcd(a, b):
    if a < b:
        tmp = a
        a = b
        b = tmp

    r = a % b
    while r!=0:
        a = b
        b = r
        r = a % b
    return b

def gcd_three(a, b, c):
    temp = gcd(a, b)
    return gcd(temp, c)

K = int(input())
ans = 0

ans += sum(range(1, K+1))
ans += 6*sum([gcd(*t) for t in combinations(range(1, K+1), 2)])
ans += 6*sum([gcd_three(*t) for t in combinations(range(1, K+1), 3)])

print(ans)