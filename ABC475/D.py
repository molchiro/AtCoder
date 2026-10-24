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

primes = [[] for _ in range(8)]
for p in sieve_of_eratosthenes(9999999):
    primes[len(str(p))].append(p)

# print(primes)

S = input()

for p in primes[len(S)]:
    p_str = str(p)
    tmp1 = [set() for _ in range(26)]
    tmp2 = [set() for _ in range(10)]
    for i, s in enumerate(S):
        tmp1[ord(s)-ord('a')].add(p_str[i])
        tmp2[int(p_str[i])].add(s)

    # print(p, tmp1, tmp2)

    if max([len(e) for e in tmp1]) == 1 and max([len(e) for e in tmp2]) == 1:
        print(p)
        exit()
    # input()

print(-1)