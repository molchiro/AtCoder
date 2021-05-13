S = input()

A = []
s = -1
f = 0
for i in range(len(S)):
    if S[i].isupper():
        if f:
            A.append(S[s:i+1])
            f = 0
        else:
            s = i
            f = 1
A.sort(key=lambda x: x.lower())
print(''.join(A))