N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

prev = -1
ans = 0
for a in A:
    ans += B[a-1]
    if a == prev + 1:
        ans += C[prev-1]
    prev = a
print(ans)
