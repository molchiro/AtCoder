N = int(input())
f = False
for i in range(9):
    for j in range(9):
        if (i+1)*(j+1) == N:
            f = True
if f:
    print('Yes')
else:
    print('No')