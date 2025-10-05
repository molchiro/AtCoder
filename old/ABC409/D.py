T = int(input())
for _ in range(T):
    N = int(input())
    S = input()

    if N == 1:
        print(S)
        continue

    f = 0
    pending = None
    for i in range(N-1):
        if f:
            print(S[i], end='')
        elif pending:
            if ord(pending) < ord(S[i]):
                print(pending, end='')
                f = 1
            print(S[i], end='')
        else:
            if ord(S[i]) <= ord(S[i+1]):
                print(S[i], end='')
            else:
                pending = S[i]
        
    if f == 0 and pending:
        if ord(pending) < ord(S[-1]):
            print(pending, end='')
            print(S[-1], end='')
        else:
            print(S[-1], end='')
            print(pending, end='')
    else:
            print(S[-1], end='')

            
    print()