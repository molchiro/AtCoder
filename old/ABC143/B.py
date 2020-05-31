N = int(input())
d = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(N-i-1):
        ans += d[i] * d[i+j+1]

print(ans)