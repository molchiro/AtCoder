N = int(input())
ans = 0
ans_d = 0
for _ in range(N):
    A, B = list(map(int, input().split()))
    ans += A
    ans_d = max(ans_d, B-A)

print(ans+ans_d)