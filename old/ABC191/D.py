from math import ceil, floor, isqrt
from decimal import Decimal, ROUND_HALF_UP

X, Y, R = list(map(lambda x: int(Decimal(Decimal(x)*10000).quantize(Decimal("0"), rounding=ROUND_HALF_UP)), input().split()))
ans = 0
for y in range(ceil((Y-R)/10000), floor((Y+R)/10000)+1):
    y *= 10000
    Z2 = R**2-(Y-y)**2
    Z = isqrt(Z2)
    l = (X-Z+9999)//10000
    r = (X+Z)//10000
    ans += r-l+1
print(ans)