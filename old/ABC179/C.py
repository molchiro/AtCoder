N = int(input())
ans = 0
for i in range(1, N):
    for j in range(i, N//i+1):
        # print(i, j)
        if i*j < N:
            if i == j:
                ans += 1
            else:
                ans += 2
        else:
            break
print(ans)