N = int(input())

s = set()
ans = 0
for i in range(N, 0, -1):
    if i not in s:
        ans += 1
        if i%3 == 0:
            s.add((i//3)*2)
            s.add(i//3)
        elif i%2==0:
            s.add(i//2)

print(ans)