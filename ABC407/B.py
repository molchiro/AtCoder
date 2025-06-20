X, Y = list(map(int, input().split()))
ans = 0
for i in range(1, 7):
    for j in range(1, 7):
        if i+j >= X or abs(i-j) >= Y:
            ans += 1
# print(ans)
print(ans/36)