N = int(input())
employees = [list(map(int, input().split())) for _ in range(N)]
ans = float('inf')
# 仕事Aをiが担当、Bをjが担当する
for i in range(N):
    for j in range(N):
        A = employees[i][0]
        B = employees[j][1]
        if i == j:
            ans = min(A+B, ans)
        else:
            ans = min(max(A, B), ans)
print(ans)