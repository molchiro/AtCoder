N, Q = list(map(int, input().split()))
place = [i for i in range(N)]
nest = [1]*N
ans = 0
for _ in range(Q):
    query = input()
    if query == '2':
        print(ans)
    else:
        _, P, H = list(map(lambda x: int(x) - 1, query.split()))

        if nest[place[P]] == 2:
            ans -= 1
        
        nest[place[P]] -= 1
        place[P] = H
        nest[H] += 1

        if nest[H] == 2:
            ans += 1
            