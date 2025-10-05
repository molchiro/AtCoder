X, Y = list(map(int, input().split()))
ans = (X+Y)%12
if ans == 0:
    ans = 12
print(ans)