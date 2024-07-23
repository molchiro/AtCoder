N, L, R = list(map(int, input().split()))


ans = []
for i in range(L-1):
    ans.append(i+1)

for i in range(R-L+1):
    ans.append(R-i)

for i in range(R, N):
    ans.append(i+1)

print(*ans)