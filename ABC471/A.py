A, B = list(map(int, input().split()))
if 9 in [A+B, A-B, A*B, A/B]:
    print('Nine')
else:
    print('Nein')