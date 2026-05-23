from atcoder.modint import Modint, ModContext
from collections import Counter
from collections import defaultdict

def sieve_of_eratosthenes(x):
    nums = [i for i in range(x+1)]

    root = int(pow(x,0.5))
    for i in range(2,root + 1):
        if nums[i] != 0:
            for j in range(i, x+1):
                if i*j >= x+1:
                    break
                nums[i*j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes

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

primes = sieve_of_eratosthenes(10**7)
# print(primes)

mod = 998244353
with ModContext(mod):

    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        primes_n = defaultdict(lambda : [0])
        A_prime_factorized = []

        for a in A:
            x = prime_factorize(a)
            counter = Counter(x)
            A_prime_factorized.append(counter)

            for k, v in counter.items():
                primes_n[k].append(v)
                # print(k, v)
        
        # print(primes_n)

        base = Modint(1)
        for k, counter in primes_n.items():
            counter.sort()
            v = counter[-1]
            base *= Modint(k**v)
        # print(base.val())

        ans = []
        el_top_inv = {k: Modint(k**(l[-1])).inv() for k, l in primes_n.items()}
        el_second_val = {k: Modint(k**(l[-2])) for k, l in primes_n.items()} 

        for counter in A_prime_factorized:
            tmp = Modint(base.val())
            for k, v in counter.items():
                if primes_n[k][-1] == v:
                    tmp *= el_top_inv[k]
                    tmp *= el_second_val[k]
            ans.append(tmp.val())
        print(*ans)

