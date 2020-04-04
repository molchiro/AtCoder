N = int(input())
A_list = list(map(int, input().split()))
A_filtered = []
for A in A_list:
    if A%2 == 1:
        A_filtered.append(A)
    else:
        if A%3 == 0 or A%5 == 0:
            A_filtered.append(A)
if len(A_filtered) == N:
    print('APPROVED')
else:
    print('DENIED')
