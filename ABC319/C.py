C = []
for _ in range(3):
    C += list(map(int, input().split()))


from itertools import permutations
kai_9 = 362880
ans = 0
for order in permutations(range(1, 10), 9):
    # print(order)
    tate = [[] for _ in range(3)]
    yoko = [[] for _ in range(3)]
    naname = [[] for _ in range(2)]
    for x in order:
        y = C[x-1]
        if x == 1:
            tate[0].append(y)
            yoko[0].append(y)
            naname[0].append(y)
        elif x == 2:
            tate[1].append(y)
            yoko[0].append(y)
        elif x == 3:
            tate[2].append(y)
            yoko[0].append(y)
            naname[1].append(y)
        elif x == 4:
            tate[0].append(y)
            yoko[1].append(y)
        elif x == 5:
            tate[1].append(y)
            yoko[1].append(y)
            naname[0].append(y)
            naname[1].append(y)
        elif x == 6:
            tate[2].append(y)
            yoko[1].append(y)
        if x == 7:
            tate[0].append(y)
            yoko[2].append(y)
            naname[1].append(y)
        elif x == 8:
            tate[1].append(y)
            yoko[2].append(y)
        elif x == 9:
            tate[2].append(y)
            yoko[2].append(y)
            naname[0].append(y)
    
    for check in tate + yoko + naname:
        # print(check)
        if check[0] == check[1] or check[1]==check[0]:
            break
    else:
        ans += 1
    
    # input()
        
print(ans/kai_9)