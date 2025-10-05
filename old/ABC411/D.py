N, Q = list(map(int, input().split()))
queries = [input() for _ in range(Q)]

ans = []
see = -1
while queries:
    query = queries.pop()
    if query[0] == '1':
        _, p = list(map(lambda x: int(x) - 1, query.split()))
        if p != see:
            continue
        see = -1

    elif query[0] == '2':
        _, p, s = query.split()
        p = int(p)-1
        if p != see:
            continue
        ans.append(s)
    

    else:
        _, p = list(map(lambda x: int(x) - 1, query.split()))
        if see == -1:
            see = p

while ans:
    print(ans.pop(), end='')
print()