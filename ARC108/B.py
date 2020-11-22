from collections import deque

N = int(input())
s = input()
f = 0
fo = 0

if N < 3:
    print(N)
else:
    ans = N
    s = 'aa' + s
    d = deque([3, 2, 1, 0])
    for i in range(4, N+2):
        if s[i] == 'x' and s[d[0]] == 'o' and s[d[1]] == 'f':
            ans -= 3
            d.popleft()
            d.popleft()
        else:
            d.insert(0, i)
    print(ans)