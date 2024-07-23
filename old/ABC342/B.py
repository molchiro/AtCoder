N = int(input())
P = input().split()
O = {}
for i, p in enumerate(P):
    O[p] = i
# print(O)
Q = int(input())
for _ in range(Q):
    A, B = input().split()
    if O[A] < O[B]:
        print(A)
    else:
        print(B)