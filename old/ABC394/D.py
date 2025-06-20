S = input()
stack = []
for s in S:
    if s == '(':
        stack.append(s)
    elif s == '[':
        stack.append(s)
    elif s == '<':
        stack.append(s)
    elif s == ')':
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            break
    elif s == ']':
        if stack and stack[-1] == '[':
            stack.pop()
        else:
            break
    elif s == '>':
        if stack and stack[-1] == '<':
            stack.pop()
        else:
            break
    
    

else:
    if len(stack) == 0:
        print('Yes')
        exit()

print('No')