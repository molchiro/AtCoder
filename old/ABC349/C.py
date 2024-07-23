S = input()
T = input()

idx = 0
for s in S:
    if s.upper() == T[idx]:
        idx += 1
    
    if idx >= 3:
        print('Yes')
        exit()

if idx == 2 and T[-1] == 'X':
    print('Yes')
else:
    print('No')