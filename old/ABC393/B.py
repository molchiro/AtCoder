S = input()
T = S+'X'*1000

ans = 0
for i in range(len(S)):
    for d in range(1, len(S)):
        if T[i] == 'A' and T[i+d*1] == 'B' and T[i+d*2] == 'C':
            ans += 1

print(ans)