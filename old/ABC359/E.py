N = int(input())
H = list(map(int, input().split()))

# (幅, 高さ)
stack = []
ans = []
now = 0
for i, h in enumerate(H):
    w = 0
    while stack and stack[-1][1] < h:
        x, y = stack.pop()
        now += x * (h-y)
        w += x
    stack.append((w, h))
    stack.append((1, h))
    now += h
    ans.append(now+1) 
    # print(stack)
        
print(*ans)