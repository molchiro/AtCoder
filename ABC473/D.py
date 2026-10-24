N, K = list(map(int, input().split()))
ans = []
tmp = []
def check(i, rem):
    global N, K
    global ans, tmp

    # print(i, rem, tmp)

    if i <= 0:
        if rem == 0:
            ans.append(tmp[:])
        return

    if i > rem:
        if rem == 0:
            ans.append(tmp+[0]*(N-len(tmp)))
        return
        
        
    for n in range(rem//i+1):
        tmp.append(n)
        check(i-1, rem-i*n)
        tmp.pop()


check(N, K)
ans = [row[::-1] for row in ans]
ans.sort()
for a in ans:
    print(*a)