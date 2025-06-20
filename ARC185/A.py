T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    S = (N+1)*N
    # print('debug',N, M,  S, S%M)
    if S%M == 0:
        print('Alice')
    elif S%M > N:
        print('Alice')
    else:
        print('Bob')