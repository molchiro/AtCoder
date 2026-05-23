A = list(map(int, input().split()))
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']

diff = []
for i in range(len(A)-1):
    diff.append(A[i+1] - A[i])
print(diff)
for i in range(26):
    ans = chr(ord('a')+i)
    now = i
    for d in diff:
        now += d
        now %= 25
        # if now == 25:
        #     if d > 0:
        #         now = 0
        #     else:
        #         now = 24
        ans += l[now]
    print(ans)
    print()
