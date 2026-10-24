S1 = input()
S2 = input()
S3 = S1[0] + S2[0]
S4 = S1[1] + S2[1]
f = 0
if 'AD' in [S1, S2, S3, S4]:
    f = 1
if 'DA' in [S1, S2, S3, S4]:
    f = 1

print('Yes' if f else 'No')