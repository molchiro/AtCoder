L, R = list(map(int, input().split()))

# 素数冪の数を数える

# 素数冪判定と合成数判定に使う素数を列挙
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

primes = sieve_of_eratosthenes(int(pow(R, 0.5))+1)

# Lより大きい区間篩で素数を数える
sieve = [1]*(R-L)
for prime in primes:
    x = prime * max((L//prime + 1), 2 )
    while x <= R:
        sieve[x-L-1] = 0
        x += prime

# print(primes, sieve)


ans = sum(sieve)

# Lより大きい素数冪を数える
for prime in primes:
    x = prime * prime
    while x <= L:
        x *= prime
    
    while x <= R:
        ans += 1
        x *= prime

print(ans + 1)