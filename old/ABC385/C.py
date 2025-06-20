N = int(input())
H = list(map(int, input().split()))

ans = 1
for i in range(N):
    h = H[i]
    for d in range(1, N-i):
        tmp = 1
        idx = i+d
        while idx < N and H[idx] == h:
            tmp += 1
            idx += d
        ans = max(ans, tmp)
print(ans)