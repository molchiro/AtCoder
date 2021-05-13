from math import gcd

N = int(input())

ans = 1
for i in range(2, N+1):
    ans = ans*i//gcd(ans, i)
ans += 1

print(ans)