N = int(input())
T = input()

if N == 1:
    if T == '1':
        print(10**10*2)
    else:
        print(10**10)
else:
    Te = T[:2]
    if Te == '10':
        T = '1' + T
        N += 1
    elif Te == '01':
        T = '11' + T
        N += 2
    seq_n = (N+3-1)//3
    if ('110'*seq_n)[:N] == T:
        print(10**10-seq_n+1)
    else:
        print(0) 