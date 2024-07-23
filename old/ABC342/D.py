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

N = int(input())
A = list(map(int, input().split()))

from collections import Counter, defaultdict
d = defaultdict(int)
for a in A:
    if a == 0:
        d[(0,)] += 1
    elif a == 1:
        d[(1,)] += 1
    else:
        c = Counter(prime_factorize(a))
        t = tuple([k for k, v in c.items() if v%2])
        d[t] += 1

# print(d)

ans = 0

for k, v in d.items():
    if k == (0,):
        for i in range(v):
            ans += N-i-1
    elif k == (1,):
        ans += v*(v-1)//2
        ans += v*d[tuple()]
    else:
        ans += v*(v-1)//2

print(ans)
