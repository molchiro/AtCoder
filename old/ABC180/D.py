X, Y, A, B = list(map(int, input().split()))
ex = 0
while X*A < Y and X*(A-1) < B:
    X *= A
    ex += 1

ex += (Y-X-1)//B

print(ex)