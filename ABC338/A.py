S = input()
f = 1
if S[0].islower():
    f = 0
for s in S[1:]:
    if s.isupper():
        f = 0

print('Yes' if f else 'No')