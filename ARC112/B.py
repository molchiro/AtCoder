B, C = list(map(int, input().split()))

# -abs(B), abs(B)
ans = 2 if B != 0 else 1

# -abs(B) < x < abs(B)
C_ = C
if B < 0:
    C_ -= 1
if abs(B)-1 < C_//2:
    ans += max(2*abs(B) - 1, 0)
elif C_%2:
    ans += 2*(C_//2)
else:
    ans += max(2*(C_//2) - 1, 0)

# x < -abs(B) or x > abs(B)
C_ = C
if B > 0:
    C_ -= 1
if C_%2:
    ans += 2*(C_//2)
else:
    ans += max(2*(C_//2) - 1, 0)

print(ans)