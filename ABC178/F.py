from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


f = True
A_Counter = Counter(A)
B_Counter = Counter(B)
for a in A_Counter.keys():
    if N-A_Counter[a] < B_Counter[a]:
        f = False

if f:
    print('Yes')
    B.sort(reverse=True)
    n = 0
    sw = True
    for i in range(N):
        if A[i] == B[i]:
            if sw:
                B[i], B[n] = B[n], B[i]
                sw = False
            else:
                B[i], B[-1-n] = B[-1-n], B[i]
                n += 1
                sw = True
    print(*B)
else:
    print('No')