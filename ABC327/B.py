B = int(input())
A = 1
while True:
    x =A**A
    if x == B:
        print(A)
        exit()
    elif x > B:
        print(-1)
        exit()
    A += 1