N = int(input())

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

primes = sieve_of_eratosthenes(10**7)

ans = 0

l = 0
while True:
    if primes[l]**4 > N:
        break
    
    if primes[l]**8 <= N:
        # print(primes[l]**8)
        ans += 1
    
    r = l + 1
    a2 = primes[l]**2
    while a2*primes[r]**2 <= N:
        # print(a2*primes[r]**2)
        ans += 1
        r += 1
    
    l += 1

print(ans)

        
    

