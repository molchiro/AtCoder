N = int(input())
H = list(map(int, input().split()))

ans = []
stack = []
for i in range(N):
    ans.append(len(stack))
    h = H[N-1-i]
    while stack and  h > stack[-1]:
        stack.pop()
    stack.append(h)
    # print(*stack)

print(*ans[::-1])
    