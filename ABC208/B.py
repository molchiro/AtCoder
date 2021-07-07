P = int(input())
coins = [1]
for i in range(1, 10):
    coins.append(coins[i-1]*(i+1))
ans = 0
for c in coins[::-1]:
    r = min(100, P//c)
    ans += r
    P -= c*r

print(ans)
