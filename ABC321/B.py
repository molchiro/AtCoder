N, X = list(map(int, input().split()))
A = list(map(int, input().split()))
for i in range(101):
    res = sum(sorted(A+[i])[1:N-1])
    if res >= X:
        print(i)
        exit()
else:
    print(-1)