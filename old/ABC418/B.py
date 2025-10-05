S = input()
ans = 0
for i in range(len(S)-1):
    for j in range(i+1, len(S)):
        if j-i+1 < 3:
            continue
        t = S[i:j+1]
        # print(t)
        if t[0] != 't' or t[-1] != 't':
            continue

        t = t[1:-1]

        ans = max(ans, t.count('t') / len(t))
print(ans)