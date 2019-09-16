A, B = list(map(int, input().split()))

d = abs(A-B)

cnt = 0
while d != 0:
    if d > 10:
        d -= 10
        cnt += 1
    elif d == 10 or d == 5 or d == 1:
        cnt += 1
        break
    elif d == 7 or d == 3 or d == 8:
        cnt += 3
        break
    else:
        cnt += 2
        break
print(cnt)
