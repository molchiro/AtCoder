K = int(input())
ans = 0
for i in range(1, K+1):
    K_ = K//i
    for j in range(1, int(K_**0.5+1)):
        k = K_//j
        # print(i, j, K_//j)
        ans += max(0, k-j+1)*2 - 1
    # if i**3 <= K:
    #     ans -= 2
    # print(ans)
print(ans)