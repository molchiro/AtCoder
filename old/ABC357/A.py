N, M = list(map(int, input().split()))
H = list(map(int, input().split()))
ans = 0
for h in H:
    if M >= h:
        ans += 1
    M -= h

print(ans)