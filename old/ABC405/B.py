N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = 0
while all([i in A for i in range(1, M+1)]):
    A.pop()
    ans += 1
print(ans)