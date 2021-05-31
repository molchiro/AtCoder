from bisect import bisect_right
N, K = list(map(int, input().split()))
friends = [list(map(int, input().split())) for _ in range(N)]
friends.sort()
# print(friends)
vil_has_friends = [0]
money_cumsum = [K]
for A, B in friends:
    if A != vil_has_friends[-1]:
        vil_has_friends.append(A)
        money_cumsum.append(money_cumsum[-1])
    money_cumsum[-1] += B
# print(vil_has_friends)
# print(money_cumsum)
money = 0
prev_money = -1
while money != prev_money:
    prev_money = money
    money = money_cumsum[bisect_right(vil_has_friends, money)-1]
print(money)