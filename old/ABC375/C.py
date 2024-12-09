N = int(input())
A = [input() for _ in range(N)]

ans = [[None]*N for _ in range(N)]

for i in range(N//2):
    if i%4 == 0:
        A_now = (N-1-i, i)
        A_d = [(-1, 0), (0, 1), (1, 0), (0, -1),]
    elif i%4 == 1:
        A_now = (N-1-i, N-1-i)
        A_d = [(0, -1), (-1, 0), (0, 1), (1, 0) ]
    elif i%4 == 2:
        A_now = (i, N-1-i)
        A_d = [(1, 0), (0, -1), (-1, 0), (0, 1) ]
    else:
        A_now = (i, i)
        A_d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


    B_d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    B_now = (i, i)
    for j in range(4):
        for k in range(N-i*2-1):
            ans[B_now[0]][B_now[1]] = A[A_now[0]][A_now[1]]
            B_now = (B_now[0]+B_d[j][0], B_now[1]+B_d[j][1])
            A_now = (A_now[0]+A_d[j][0], A_now[1]+A_d[j][1])

    # print()
    # for l in range(N):
    #     print(ans[l])

for i in range(N):
    print(''.join(ans[i]))


