cards = list(map(int, input().split()))
ans = 0
for c in cards:
    ans = max(ans, sum(cards) - c)
print(ans)