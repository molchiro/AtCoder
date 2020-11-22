N = int(input())
s = input()

ans = N
s_ = ['*', '*']
for i in range(N):
    s_ += s[i]
    if s_[-3:] == ['f', 'o', 'x']:
        ans -= 3
        s_.pop()
        s_.pop()
        s_.pop()
print(ans)