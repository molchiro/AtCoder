N = int(input())
L = list(map(int, input().split()))

ans = 10**18

l = 0
r = sum(L)
for x in L:
    l += x
    r -= x
    ans = min(ans, abs(r-l))

print(ans)
    