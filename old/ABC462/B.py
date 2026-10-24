N = int(input())
ans = [[] for _ in range(N)]
for i in range(N):
    K, *A = list(map(int, input().split()))
    for a in A:
        ans[a-1].append(i+1)

for row in ans:
    print(len(row), *row)