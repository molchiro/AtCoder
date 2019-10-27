import math

a, b, x = list(map(int, input().split()))
if a**2*b == x:
    theta = 90
elif a**2*b/2 > x:
    h = 2*x/a/b
    theta = math.degrees(math.atan(h/b))
else:
    h = 2*x/(a**2)-b
    theta = math.degrees(math.atan(a/(b-h)))

print(90 - theta)
