A, B = list(map(int, input().split()))
if A == B:
    print(1)
elif (B - A)%2:
    print(2)
else:
    print(3)