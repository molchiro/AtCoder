N, K = list(map(int, input().split()))
clothes = [list(map(int, input().split())) for _ in range(N)]
clothes.sort()

def judge(test):
    global N, K, clothes
    stack = [(-10**18, -10**18)]
    for l, r in clothes:
        if l - stack[-1][1] >= test:
            # 足せる時
            stack.append((l, r))
        elif l >= stack[-1][0] and  r < stack[-1][1]:
            # 入れ替えた方が有利な時
            stack.pop()
            stack.append((l, r))
    
    return len(stack)-1 > 1 and len(stack)-1 >= K


ok = 0
ng = 10**18
while ng - ok > 1:
    test = (ng+ok)//2
    if judge(test):
        ok = test
    else:
        ng = test

ans = ok
if ans == 0:
    ans = -1
print(ans)