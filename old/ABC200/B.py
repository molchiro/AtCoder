N, K = list(map(int, input().split()))
for _ in range(K):
    if N%200 == 0:
        N //=200
    else:
        N = N*1000 + 200
print(N)
