N = int(input())

balls = []
for i in range(N):
    balls.append(list(map(int, input().split())))

X = []
for i in range(N-1):
    for j in range(i+1,N):
        X.append((balls[i][0] - balls[j][0], balls[i][1] - balls[j][1]))
        X.append((balls[j][0] - balls[i][0], balls[j][1] - balls[i][1]))


Y = set(X)
res = 0
for x in X:
    res = max(res, X.count(x))
print(N-res)