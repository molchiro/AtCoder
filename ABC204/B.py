N = int(input())
A = list(map(int, input().split()))
ans = 0
for a in A:
    ans += max(0, a-10)
print(ans)