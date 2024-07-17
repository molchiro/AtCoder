N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = []

for a in A:
    C.append((a, 'A'))

for b in B:
    C.append((b, 'B'))

C.sort()

prev = ''
for c, d in C:
    if d == prev == 'A':
        print('Yes')
        break
    prev = d
else:
    print('No')