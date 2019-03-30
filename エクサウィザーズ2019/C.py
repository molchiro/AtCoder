N, Q = list(map(int, input().split()))
X = [1 for i in range(N)]
s = [x for x in input()]

res = 0
for i in range(Q):
    t, d = input().split()
    if d == 'L':
        for j in range(N):
            if s[j] == t:
                if j != 0:
                    X[j-1] += X[j]
                X[j] = 0
    else:
        for j in range(N, 0, -1):
            if s[j-1] == t:
                if j != N:
                    X[j] += X[j-1]
                X[j-1] = 0
print(sum(X))

    