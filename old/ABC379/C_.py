from heapq import heapify, heappop, heappush

N, M = list(map(int, input().split()))
X = list(map(int, input().split()))
A = list(map(int, input().split()))

hq = list(zip(X, A))
heapify(hq)

filled = 0

ans = 0
while hq:
    x, a = heappop(hq)
    # print(x, a)

    if x == filled + 1:
        ans += (a-1)*a//2
        filled += a
    elif x <= filled:
        ans += (filled-x+1)*a 
        ans += (a-1)*a//2
        filled += a
    else:
        print(-1)
        exit()

    
if filled != N:
    print(-1)
else:
    print(ans)

