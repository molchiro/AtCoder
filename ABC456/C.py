mod = 998244353

S = input()

stack = [[]]

prev = 'x'
for s in S:
    if s == prev:
        stack.append([])
    stack[-1].append(s)
    prev = s

# print(stack)

ans = 0
for group in stack:
    n = len(group)
    ans += n*(n+1)//2
    ans %= mod

print(ans)