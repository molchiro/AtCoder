A, B = list(map(int, input().split()))

if A == B:
    print(A+B)
else:
    x = max(A,B)
    print(2*x-1)