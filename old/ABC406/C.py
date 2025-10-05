N = int(input())
P = list(map(int, input().split()))

tmp = 0
stack = []
for i in range(N-1):
    if P[i] < P[i+1]:
        tmp += 1
    else:
        stack.append(tmp)
        tmp = 0
stack.append(tmp)
stack = [x for x in stack if x > 0]

ans = 0
for i in range(len(stack)-1):
    ans += stack[i]*stack[i+1]

print(ans)