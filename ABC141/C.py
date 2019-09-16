N, K, Q = list(map(int, input().split()))
M = [0 for i in range(N)]
for i in range(Q):
    M[int(input()) - 1] += 1
for m in M:
    if K - Q + m > 0:
        print('Yes')
    else:
        print('No')