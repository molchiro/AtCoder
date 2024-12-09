# 1 以上 N 以下の整数が素数かどうかを返す
def create_prime_numbers(N):
    # エラトステネスの篩で素数のリストを求める

    isprime = [1] * (N+1)
    isprime[0] = 0
    isprime[1] = 0
    for p in range(2, N+1):
        if not isprime[p]:
            continue

        q = p * 2
        while q <= N:
            isprime[q] = 0
            q += p


    return [i for i in range(N+1) if isprime[i]]

N = int(input())

ans = 0
prime_numbers = create_prime_numbers(10**6)
# print(len(prime_numbers))
for i in range(len(prime_numbers)-1):
    p = prime_numbers[i]

    ok = i
    ng = len(prime_numbers)+1
    while ng - ok > 1:
        test = (ng+ok)//2
        q = prime_numbers[test]
        if p*q*q*q <= N:
            ok = test
        else:
            ng = test

    ans += ok-i

print(ans)