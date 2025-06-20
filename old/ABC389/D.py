R = int(input())
RR4 = R*R*4

x = 10**6+1
y = 1
ans = 1
while y <= R:
    while x >= 0 and (2*x+1)**2 + (2*y+1)**2 > RR4:
        x -= 1
    if x < 0:
        break

    ans += 4*(x+1)
    y += 1

print(ans)