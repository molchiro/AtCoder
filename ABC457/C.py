N, K = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
C = list(map(int, input().split()))

for i, c in enumerate(C):
    # print(c, K)
    L = A[i][0]
    if K > L*c:
        K-= L*c
    else:
        K -= 1
        K %= L
        print(A[i][K+1])
        break