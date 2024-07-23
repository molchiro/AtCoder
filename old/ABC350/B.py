N, Q = list(map(int, input().split()))
T = list(map(lambda x: int(x) - 1, input().split()))
ans = [1]*N

for t in T:
    ans[t] = (ans[t]+1)%2

print(sum(ans))