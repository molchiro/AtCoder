N, M, T = list(map(int, input().split()))
N_max = N
prev = 0

f = 1
for _ in range(M):
    A, B = list(map(int, input().split()))
    N -= A-prev
    if N <= 0:
        N = 0
        f = 0
    N = min(N_max, N+B-A)
    prev = B
N -= T-prev
if N <= 0:
    N = 0
    f = 0
print('Yes' if f else 'No')