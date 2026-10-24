N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = sorted(A)
C = [int(A[i]!=B[i]) for i in range(N)]
# print(C)
cumsum = [0]
for c in C:
    cumsum.append(cumsum[-1]+c)

for i in range(N-K):
    if cumsum[i] + (cumsum[-1]-cumsum[i+K]) == 0:
        print('Yes')
        break
else:
    print('No')