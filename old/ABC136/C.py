N = int(input())
H = list(map(int, input().split()))

min_H = 0
f = True
for i in range(N):
    if min_H > H[i]:
        f = False
        break
    else:
        if min_H < H[i]:
            min_H = H[i]-1
if f:
    print('Yes')
else:
    print('No')
