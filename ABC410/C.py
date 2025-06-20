N, Q = list(map(int, input().split()))
A = [i+1 for i in range(N)]
offset = 0
for _ in range(Q):
    query = input()
    if query[0] == '1':
        _, p, x = list(map(int, query.split()))
        A[(p-1 + offset)%N] = x


    elif query[0] == '2':
        _, p = list(map(int, query.split()))
        print(A[(p-1 + offset)%N])
    else:
        _, k = list(map(int, query.split()))
        offset += k

    