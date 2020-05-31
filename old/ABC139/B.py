A, B = list(map(int, input().split()))
sock = 1
ans = 0
while sock < B:
    sock += A - 1
    ans += 1
print(ans)