N = int(input())

f = 0
prev = ''
for _ in range(N):
    if f:
        print('No')
        break
    S = input()
    if prev == 'sweet' and S == 'sweet':
        f = 1
    prev = S
else:
    print('Yes')