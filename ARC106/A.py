N = int(input())
B = 1
while 5**B < N:
    N_ = N - 5**B
    A = 0
    while N_%3 == 0:
        N_ //= 3
        A += 1
        if N_ == 1:
            print(A, B)
            exit()
    B += 1

print(-1)
