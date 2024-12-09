N = int(input())
l_pre = None
r_pre = None
ans = 0
for _ in range(N):
    A, S = input().split()
    if S == 'L':
        if l_pre != None:
            ans += abs(int(A) - l_pre)
        l_pre = int(A)
    else:
        if r_pre != None:
            ans += abs(int(A) - r_pre)
        r_pre = int(A)
print(ans)