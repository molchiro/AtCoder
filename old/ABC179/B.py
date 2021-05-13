N = int(input())
n = 0
f = False
for _ in range(N):
    D1, D2 = list(map(int, input().split()))
    if D1 == D2:
        n += 1
    else:
        n = 0
    if n >= 3:
        f = True
print('Yes' if f else 'No')