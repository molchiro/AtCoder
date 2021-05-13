N = int(input())
ans = 0
for _ in range(N):
    A, B = list(map(int, input().split()))
    ans += (A+B)*(B-A+1)//2
print(ans)