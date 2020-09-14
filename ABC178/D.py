mod = 10**9+7

def f(a, b):
    if a == 0 or b == 0:
        return 1
    if a < b:
        a, b = b, a
    x = 1
    y = 1
    for i in range(b):
        x *= (a+b-i)
        y *= b-i
    return (x//y)%mod


S = int(input())

ans = 0
i = 1
while True:
    rem = S - i*3
    if rem < 0:
        break
    ans += f(rem, i-1)
    ans %= mod
    i += 1

print(ans)