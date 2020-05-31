S = input()
ans = [0 for i in range(len(S))]

odd = 0
even = 0
for i in range(len(S)):
    if S[i] == 'R':
        tmp = even
        even = odd + 1
        odd = tmp
    else:
        ans[i-1] += even
        ans[i] += odd
        odd = 0
        even = 0

for i in range(len(S)):
    if S[-i-1] == 'L':
        tmp = even
        even = odd + 1
        odd = tmp
    else:
        ans[-i] += even
        ans[-i-1] += odd
        odd = 0
        even = 0

print(*ans)
