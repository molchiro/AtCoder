N, T, P = list(map(int, input().split()))
L = list(map(int, input().split()))
i = 0
while  sum([1 if l >= T else 0 for l in L]) < P:
    i += 1
    for j in range(N):
        L[j] += 1

print(i)