from math import gcd

def extGCD(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = extGCD(b, a%b)
    return g, y, x-a//b*y

T = int(input())
for _ in range(T):
    N, S, K = list(map(int, input().split()))
    g = gcd(gcd(N, S), K)
    N, S, K = N//g, S//g, K//g
    # Kx ≡ S (mod N)
    # x ≡ K^-1*S (mod N)
    # K*K^-1 ≡ 1 (mod N)
    # K*K^-1 - 1 = yN
    # K*x - Ny = 1 (x = K^-1)
    if gcd(K, N) != 1:
        print(-1)
    else:
        K_inv = extGCD(K, -N)[1]
        print((S*K_inv)%N)
