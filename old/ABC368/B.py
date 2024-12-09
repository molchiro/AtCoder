N = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = 0
while sum([1 if x > 0 else 0 for x in A]) > 1:
    A.sort(reverse=True)
    A[0] -= 1
    A[1] -= 1
    ans += 1
print(ans)