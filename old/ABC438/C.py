N = int(input())
A = list(map(int, input().split()))
stack = []
for i in range(3):
    stack.append(-1)

for a in A:
    stack.append(a)
    if stack[-1] == stack[-2] == stack[-3] == stack[-4]:
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()

print(len(stack)-3)