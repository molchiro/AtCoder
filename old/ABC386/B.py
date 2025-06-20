S = input() + 'x'
ans = 0
i = 0
while i < len(S)-1:
    ans += 1
    if S[i] == S[i+1] == '0':
        i += 2
    else:
        i += 1
print(ans)