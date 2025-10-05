from collections import Counter

xxxx = 10**4

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

X = int(input())
ans = []
tmp = 1
i = 1
while tmp < xxxx:
    n = tmp - 1
    c = Counter(prime_factorize(n**2 + n + X))
    if all([v%2 == 0 for v in c.values()]):
        ans.append(n)

    tmp += i
    i += 2
    print(tmp-1)

print(len(ans))
print(*ans)