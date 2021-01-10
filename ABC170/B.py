X, Y = list(map(int, input().split()))
b = (Y-2*X)/2
a = X-b
if a*b>=0 and int(a) == a and int(b)==b:
    print('Yes')
else:
    print('No')