N = int(input())
S = input()

ans = [None]*N
head = 0
tail = N-1
f = 0
for i in range(N):
    if S[N-1-i] == 'o':
        f = (f+1)%2
    
    if f:
        ans[head] = N-i
        head += 1
    else:
        ans[tail] = N-i
        tail -= 1

print(*ans)