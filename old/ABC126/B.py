S = input()
F = int(S[:2])
R = int(S[2:])
FF = 0 < F and F < 13
RR = 0 < R and R < 13

if FF and RR:
    print('AMBIGUOUS')
elif FF:
    print('MMYY')
elif RR:
    print('YYMM')
else:
    print('NA')