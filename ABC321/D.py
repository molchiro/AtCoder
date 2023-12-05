N, M, P = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
idx = M-1
ans = 0
accum = sum(B)
for a in A:
    while idx >= 0 and a+B[idx] > P:
        accum -= B[idx]
        idx -= 1
    ans += a*(idx+1) + accum + P*(M-idx-1)
print(ans)