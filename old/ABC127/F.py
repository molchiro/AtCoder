Q = int(input())

dum, a, b = list(map(int, input().split()))
aL = a
aR = a
B = b

for i in range(Q-1):
    q = input()
    if q == '2':
        print(aL, B)
    else:
        dum, a, b = list(map(int, q.split()))
        if a < aL:
            B += aL - a
            aR = aL
            aL = a
        elif a > aR:
            B += a - aR
            aL = aR
            aR = a
        else:
            aL = a
            aR = a
        B += b