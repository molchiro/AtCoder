N = int(input())
l = 0
ans = ''
for _ in range(N):
    C, L = input().split()
    l += int(L)
    if l > 100:
        print('Too Long')
        break
    ans += C*int(L)
else:
    print(ans)