def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

N = int(input())
prime_factors = factorization(N)
if prime_factors[0][0] == 1:
    print(0)
else:
    ans = 0
    for pf in prime_factors:
        n = pf[1]
        i = 0
        while n >= i:
            n -= i
            i += 1
        ans += i-1
    print(ans)