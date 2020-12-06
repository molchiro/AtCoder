N = int(input())
T = input()
if N == 1:
    if T == '1':
        ans = (10**10*2)
    else:
        ans = (10**10)
elif N == 2:
    if T == '00':
        ans = (0)
    elif T == '11':
        ans =(10**10)
    elif T == '10':
        ans =(10**10)
    else:
        ans = (10**10-1)
else:
    ans = 0
    if T[:2] == '00':
        print(0)
        exit()
    elif T[:2] == '10':
        T = '1'+T
        N += 1
    elif T[:2] == '01':
        T = '11'+T
        N += 2
    UNIT = '110'*((N+3-1)//3)
    if UNIT[:N] == T:
        ans = 10**10 - (N+3-1)//3 + 1
    else:
        ans = 0

print(ans)