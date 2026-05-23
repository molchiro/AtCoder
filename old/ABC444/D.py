N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

ans = []
tmp = 0
for i in range(1, 200010):
    while A and A[-1] < i:
        N -= 1
        A.pop()
    tmp += N
    # print(tmp)
    if N == 0 and tmp == 0:
        break
    ans.append(str(tmp%10))
    tmp //= 10
print(''.join(ans[::-1]))
