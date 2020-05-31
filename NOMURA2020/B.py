S = list(input())
for i in range(len(S)):
    if S[i] =='?':
        S[i] = 'D'
print(''.join(S))