N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = [0]*N
for a in A:
    ans[a-1] = 1

print(N-M)
print(*[i+1 for i, v in enumerate(ans) if v == 0])