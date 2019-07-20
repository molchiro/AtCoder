N = int(input())
A = [int(input()) for i in range(N)]

FIRST = max(A)
if A.count(FIRST) > 1:
    for i in range(N):
        print(FIRST)
else:
    SECOND = max([a for a in A if a != FIRST])
    for a in A:
        if a == FIRST:
            print(SECOND)
        else:
            print(FIRST)