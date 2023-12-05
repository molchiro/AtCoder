from math import floor, ceil

D = int(input())
ans = float('inf')
for x in range(10**6+1):
    xx = x**2
    if xx > D:
        break
    tmp = D - xx
    tmp = tmp**0.5
    ans = min(ans, abs(xx+ceil(tmp)**2-D))
    ans = min(ans, abs(xx+floor(tmp)**2-D))
print(ans)