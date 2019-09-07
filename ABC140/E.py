N = int(input())
P = list(map(int, input().split()))
remainder = [i + 1 for i in range(N)]
ans = 0
for i in range(N):
    temp = remainder[:]
    for j in range(N-i-1):
        ans += temp[-2]
        temp.remove(P[-1-j])
    remainder.remove(P[i])
print(ans)