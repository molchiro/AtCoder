N = int(input())
ans = 0
for i in range(1, N+1):
    x = N//i
    ans += x*(x+1)*i/2
print(int(ans))

list(map(int, input().split()))