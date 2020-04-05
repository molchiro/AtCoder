N = int(input())
R = []
B = []
for i in range(N):
    X, C = input().split(' ')
    if C == 'R':
        R.append(int(X))
    else:
        B.append(int(X))
R.sort()
B.sort()
if len(R) > 0: print(*R, sep='\n')
if len(B) > 0: print(*B, sep='\n')