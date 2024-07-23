S = input()
if S[0] == '<' and set(list(S[1:len(S)-1])) == {'='} and S[-1] == '>':
    print('Yes')
else:
    print('No')