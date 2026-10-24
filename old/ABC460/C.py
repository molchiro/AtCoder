N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

ans = 0
for a in A:
    if B[-1] > 2*a:
        continue

    ans += 1
    B.pop()
    if len(B) <= 0:
        break

print(ans)