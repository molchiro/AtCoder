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

LIMMIT = 10**12

primes = sieve_of_eratosthenes(5*100000+1)
doubled_primes = [x*x for x in primes]
# print(len(primes))
# print(primes[-1])
l = len(primes)
nums = []
for i in range(l-1):
    a = doubled_primes[i]
    for j in range(i+1, l):
        b = doubled_primes[j]

        if a*b > LIMMIT:
            break

        c = a
        while c <= LIMMIT+1:
            d = c*b
            if d > 10**12:
                break
            while d <= LIMMIT+1:
                nums.append(d)
                d *= b
            c *= a

nums.append(LIMMIT+1)
nums.sort()

# print(len(nums))
# print(nums[:100])



# print(l)
from bisect import bisect_left, bisect_right

Q = int(input())
for _ in range(Q):
    A = int(input())
    idx = bisect_right(nums, A)
    if nums[idx] > A:
        idx -= 1
    print(nums[idx])

