S = input()
ans = 0
for i in range(10000):
    password = ('0000'+str(i))[-4:]
    f = 1
    for i in range(10):
        if S[i] == 'o':
            if not str(i) in password:
                f = 0
        elif S[i] == 'x':
            if str(i) in password:
                f = 0
    if f:
        ans += 1
print(ans)