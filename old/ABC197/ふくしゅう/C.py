N = int(input())
A = list(map(int, input().split()))

ans = float('inf')
for i in range(1<<(N-1)):
    i |= 1<<(N-1)
    or_accum = 0
    xor_accum = 0
    for j in range(N):
        or_accum |= A[j]
        if i>>j & 1:
            xor_accum ^= or_accum
            or_accum = 0
    ans = min(ans, xor_accum)

print(ans)
