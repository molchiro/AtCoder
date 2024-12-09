N = int(input())
H = list(map(int, input().split()))

T = 0

for h in H:

    x = h//5
    # print(T, h, x)
    T += 3*x
    h -= 5*x

    if h <= 0:
        continue

    while h > 0:
        T += 1
        if T%3 == 1:
            h -= 1
        elif T%3 == 2:
            h -= 1
        else:
            h -= 3
    
    # print(T, h)

print(T)
