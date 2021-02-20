S = input()
f = 1
for i in range(len(S)):
    if i%2:
        if S[i].islower():
            f = 0
    else:
        if S[i].isupper():
            f = 0
print('Yes' if f else 'No')