A = [list(map(int, input().split())) for i in range(3)]
A = A[0] + A[1] + A[2]
N = int(input())
for i in range(N):
    b = int(input())
    if b in A:
        A[A.index(b)] = 0
lines = [
            [A[0], A[3], A[6]],
            [A[1], A[4], A[7]],
            [A[2], A[5], A[8]],
            [A[0], A[1], A[2]],
            [A[3], A[4], A[5]],
            [A[6], A[7], A[8]],
            [A[0], A[4], A[8]],
            [A[2], A[4], A[6]],
        ]
if [0, 0, 0] in lines:
    print('Yes')
else:
    print('No')