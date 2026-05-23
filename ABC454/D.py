T = int(input())

for _ in range(T):
    A = input()
    B = input()

    C = ['y', 'y', 'y']
    for a in A:
        C.append(a)
        if C[-4] == '(' and C[-3] == 'x' and C[-2] == 'x' and C[-1] == ')':
            C.pop()
            C.pop()
            C.pop()
            C.pop()
            C.append('x')
            C.append('x')

    
    D = ['y', 'y', 'y']
    for b in B:
        D.append(b)
        if D[-4] == '(' and D[-3] == 'x' and D[-2] == 'x' and D[-1] == ')':
            D.pop()
            D.pop()
            D.pop()
            D.pop()
            D.append('x')
            D.append('x')
    

    # print(C)
    # print(D)

    print('Yes' if C == D else 'No')