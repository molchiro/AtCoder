lim = 10**6

N = int(input())
A = list(map(int, input().split()))

rest = [0]*(lim + 1)
ans = [0]*(lim + 1)
for i in range(lim, 0, -1):
    # 取り出し
    if A and A[-1] == i:
        A.pop()
        rest[i] = 1
    
    # 繋げるペアがあるかチェック
    j = i
    s = []
    while j <= lim:
        if rest[j]:
            s.append(j)
        
        j += i
    
    if len(s) >= 2:
        # s.pop()
        for e in s[1:]:
            ans[e] = max(ans[e], i)

print(sum(ans))