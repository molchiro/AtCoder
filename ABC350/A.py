S = input()
a = S[:3]
b = int(S[3:])

if a == 'ABC' and 1 <= b <= 349 and b != 316:
    print('Yes')
else:
    print('No')