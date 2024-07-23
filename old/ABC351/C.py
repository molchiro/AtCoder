N = int(input())
A = list(map(int, input().split()))
ans = []

for a in A:
    ans.append(a)
    while len(ans) > 1 and ans[-1] == ans[-2]:
        ans.pop()
        ans[-1] += 1
    # print(ans)
print(len(ans))