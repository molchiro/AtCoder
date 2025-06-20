N, X = int(input())
A = list(map(int, input().split()))
A_sorted = sorted(A)

k_last = N-1
while A_sorted[0]+A_sorted[1]+A_sorted[k_last] > X:
    k_last -= 1
    
for i in range(N-2):
    Ai = A_sorted[i]

    for j in range(i+1, N-1):
        Aj = A_sorted[j]



print(-1)