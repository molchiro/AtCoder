T, X = list(map(int, input().split()))
A = list(map(int, input().split()))

prev = 10**18

for i, a in enumerate( A):
    if abs(prev-a) >= X:
        print(i, a)

        prev = a