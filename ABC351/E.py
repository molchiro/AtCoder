N = int(input())
odds = []
evens = []
for _ in range(N):
    X, Y = list(map(int, input().split()))
    if (X+Y)%2:
        odds.append((X, Y))
    else:
        evens.append((X, Y))


def culc(points):
    res = 0
    for i in range(len(points)-1):
        for j in range(1, len(points)):
            xi, yi = points[i]
            xj, yj = points[j]
            res += max(abs(xj-xi), abs(yi-yj)) 
    
    return res


print(culc(odds)+culc(evens))
            