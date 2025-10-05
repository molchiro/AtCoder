S = input()
T = input()

ans = True
for i in range(len(S)-1):
    if S[i+1].isupper():
        if not S[i] in T:
            ans = False

print('Yes' if ans else 'No')