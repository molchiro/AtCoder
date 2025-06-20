S = list(input())

for i in range(len(S)-1):
    if S[-2-i] == 'W' and S[-1-i] == 'A':
        S[-2-i] = 'A'
        S[-1-i] = 'C'

print(''.join(S))