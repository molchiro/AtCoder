N, S, M, L = list(map(int, input().split()))
ans = float('inf')
for l in range(N+1):
    for m in range(N+1):
        for s in range(N+1):
            if 6*s + 8*m + 12*l >= N:
                ans = min(ans, s*S + m*M + l*L)
print(ans)