X, Y, Z = list(map(int, input().split()))
a = (X-Z*Y) / (Z-1)

if a >= 0 and int(a) == a:
    print('Yes')
else:
    print('No')