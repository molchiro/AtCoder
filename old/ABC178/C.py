mod = 10**9+7

N = int(input())
a = 1
b = 1
c = 1
for _ in range(N):
    a *= 10
    b *= 9
    c *= 8
    a %= mod
    b %= mod
    c %= mod

ans = (a -2*b + c)%mod
print(ans)