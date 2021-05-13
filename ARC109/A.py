a, b, x, y = list(map(int, input().split()))

diff = a - b
ans = 0
if diff > 0:
    ans += x
    diff -= 1
    if 2*x < y:
        ans += 2*x*diff
    else:
        ans += y*diff
else:
    diff = -diff
    ans = min(x+y*diff, x+y*(diff+1), x+2*x*diff)
print
