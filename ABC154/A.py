ST = input().split()
A, B = list(map(int, input().split()))
U = input()
idx = ST.index(U)
if idx == 0:
    print(A-1, B)
else:
    print(A, B-1)
