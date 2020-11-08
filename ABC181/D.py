from collections import Counter

S = input()

if len(S) == 1:
    print('Yes' if int(S)%8 == 0 else 'No')
elif len(S) == 2:
    print('Yes' if int(S)%8 == 0 or int(S[::-1])%8 == 0 else 'No')
else:
    C = Counter(list(S))
    for i in range(100,1000):
        if i%8:
            continue
        if '0' in list(str(i)):
            continue
        t = Counter(list(str(i)))
        hachi = True
        for e in t:
            if C[e] < t[e]:
                hachi = False
        if hachi:
            print('Yes')
            break
    else:
        print('No')