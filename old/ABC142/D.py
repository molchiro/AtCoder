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

    return arr

A, B = list(map(int, input().split()))

prime_factors_A = [x[0] for x in factorization(A)]
prime_factors_B = [x[0] for x in factorization(B)]
prime_factors_A.append(1)
prime_factors_B.append(1)
ans = 0
for x in prime_factors_A:
    ans += 1 if x in prime_factors_B else 0
print(ans)