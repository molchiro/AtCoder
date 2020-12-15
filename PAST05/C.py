digit = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N = int(input())
S = ''

for i in range(3):
    S = digit[N%36] + S
    N = N//36
    if N == 0:
        break

print(S)