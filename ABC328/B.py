N = int(input())
D = list(map(int, input().split()))
ans = 0
for i, d in enumerate(D):
    for j in range(d):
        if len(set(list(str(i+1)+str(j+1)))) == 1:
            ans += 1
print(ans)