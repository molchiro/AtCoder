D, F = list(map(int, input().split()))
now = F
while now <= D:
    now += 7
print(now-D)