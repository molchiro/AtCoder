T = int(input())
for _ in range(T):
    S = input()
    stack = ['X']*3
    for s in S[::-1]:
        stack.append(s)
        while True:
            if stack[-1]+stack[-2]+stack[-3] == 'ABC':
                for _ in range(3):
                    stack.pop()
            elif stack[-1]+stack[-2] == 'AB':
                for _ in range(2):
                    stack.pop()
            elif stack[-1] == 'A':
                stack.pop()
            else:
                break
        # print(stack)
    
    print(len(stack)-3)
    
    