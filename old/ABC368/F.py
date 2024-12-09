def solve(heaps):
    nim_sum = 0

    for stones in heaps:
        nim_sum ^= stones

    return nim_sum

N = int(input())
A = list(map(int, input().split()))

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

heaps = []
for a in A:
    heaps.append(len(prime_factorize(a)))

print('Anna' if solve(heaps) else 'Bruno')