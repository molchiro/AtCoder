X = int(input())

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        tmp = i*j
        if tmp != X:
            ans += tmp
print(ans)