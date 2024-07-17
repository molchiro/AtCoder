l = [list(map(int, input().split())) for _ in range(3)]

f = 0
for i in range(3):
    x1, y1 = l[-2+i]
    x2, y2 = l[-1+i]
    x3, y3 = l[i]
    a1 = x2-x1
    b1 = y2-y1
    a2 = x3-x2
    b2 = y3-y2
    if a1*a2 == -b1*b2:
        f = 1

print('Yes' if f else 'No')