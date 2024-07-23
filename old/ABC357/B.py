S = input()
s = len(S)
l = 0
for x in S:
    if x.isupper():
        l += 1
        s -= 1

if l > s:
    print(S.upper())

else:
    print(S.lower())


