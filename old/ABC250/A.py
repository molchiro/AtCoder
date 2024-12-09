H, W = list(map(int, input().split()))
R, C = list(map(int, input().split()))
ans = 4
if R == 1:
    ans -= 1

if R == H:
    ans -= 1
if C == 1:
    ans -= 1

if C == W:
    ans -= 1

print(ans)