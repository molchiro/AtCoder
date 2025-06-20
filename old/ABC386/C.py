K = int(input())
S = input()
T = input()

if len(S) < len(T):
    S, T = T, S

if len(S) - len(T) > 1:
    print('No')
    exit()

if len(S) == len(T):
    ct = 0
    for s, t in zip(S, T):
        if s != t:
            ct += 1
    print('Yes' if ct <= 1 else 'No')
else:
    if S[:len(S)-1] == T:
        print('Yes')
    else:
        for i in range(len(S)):
            if S[i] != T[i]:
                break
        S = S[:i] + S[i+1:]
        print('Yes' if S == T else 'No')