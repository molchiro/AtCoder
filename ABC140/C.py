N = int(input())
B = list(map(int, input().split()))
ans = 0
ans += B[0]
ans += B[-1]
for i in range(N-2):
    m = min(B[i], B[i+1])
    ans += min(B[i], B[i+1])
print(ans)