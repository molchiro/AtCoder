N, M = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
for _ in range(N):
    A, B = list(map(int, input().split()))
    A -= 1
    x = min(C[A], B)
    ans += x
    C[A] -= x
print(ans)