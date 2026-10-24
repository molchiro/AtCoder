T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = [a-i for i, a in enumerate(A)]
    ans = 0

    stack = [(-10**18, 1)]
    for b in B:
        if b == stack[-1]:
            h, w = stack.pop()
            stack.append((h, w+1))
        elif b > stack[-1]:
            stack.append((b, 1))
        else:
            k = b
            


