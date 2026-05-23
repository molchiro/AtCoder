N = int(input())
T = list(map(tuple, enumerate(map(int, input().split()))))
T.sort(key=lambda x: x[1])
ans = []
for i in range(3):
    ans.append(1+T[i][0])
print(*ans)