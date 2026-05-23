Q = int(input())
stack = []
check = [0]
accum = 0
for _ in range(Q):
    query = input()
    if query == '2':
        c = stack.pop()
        check.pop()
        if c == '(':
            accum -= 1
        else:
            accum += 1

        print('Yes' if check[-1] == 0 and accum == 0 else 'No')
        
    else:
        _, c = query.split()
        if c == '(':
            accum += 1
        else:
            accum -= 1
        stack.append(c)
        check.append(1 if check[-1] == 1 or accum < 0 else 0)

        print('Yes' if check[-1] == 0 and accum == 0 else 'No')
    
    # print(stack)
    # print(check)
    # print(accum)