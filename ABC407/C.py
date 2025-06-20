S = list(map(int, list(input())))
ans = 0
x = 0
while S:
    s = S.pop()
    s -= x
    s %= 10
    
    while s != 0:
        s -= 1
        s %= 10

        ans += 1
        x += 1
        x %= 10

    ans += 1
    # print(ans, x)
print(ans)