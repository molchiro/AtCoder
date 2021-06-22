N, K = list(map(int, input().split()))
friends = [list(map(int, input().split())) for _ in range(N)]
friends.sort()
ans = K
for village, money in friends:
    if ans < village:
        break
    ans += money
print(ans)