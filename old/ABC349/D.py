L, R = list(map(int, input().split()))
ans = []

l = L
digit = 0
while L + (1 << digit) <= R:
    if  L >> digit & 1:
        L += 1 << digit
        ans.append((l, L))
        l = L
    
    digit += 1

for i in range(digit-1, -1, -1):
    if R >> i & 1:
        L += 1 << i
        ans.append((l, L))
        l = L

print(len(ans))
for x in ans:
    print(*x)