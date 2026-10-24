N = int(input())
A = list(map(int, input().split()))
ans = [0]*3
for a in A:
    if a%1000:
        b = 1000*(a//1000 + 1) - a
        ans[2] += b//100
        b %= 100
        ans[1] += b//10
        b %= 10
        ans[0] += b

print(*ans)