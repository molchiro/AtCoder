S, A, B, X = list(map(int, input().split()))
ans = 0
while X > 0:
    t = min(X, A)
    ans += S*t
    X -= t
    X -= B
print(ans)