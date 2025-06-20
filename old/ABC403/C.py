N, M, Q = list(map(int, input().split()))

A = set()
B = [set() for _ in range(N)]

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        _, X, Y = query
        B[X-1].add(Y)
    elif query[0] == 2:
        _, X = query
        A.add(X-1)
    else:
        _, X, Y = query

        if X-1 in A:
            print('Yes')
        elif Y in B[X-1]:
            print('Yes')
        else:
            print('No')
