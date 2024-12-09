Q = int(input())
l = [0]*(10**6+1)
ans = 0
for _ in range(Q):
    args = list(map(int, input().split()))
    if args[0] == 1:
        x = args[1]
        if l[x] == 0:
            ans += 1
        l[x] += 1
    elif args[0] == 2:
        x = args[1]
        l[x] -= 1
        if l[x] == 0:
            ans -= 1
    else:
        print(ans)        
