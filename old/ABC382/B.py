N, D = list(map(int, input().split()))
S = list(input())

i = N-1
ct = 0
while ct < D:
    if S[i] == '@':
        S[i] = '.'
        ct += 1
    i -= 1

print(''.join(S))