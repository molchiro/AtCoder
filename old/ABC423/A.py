X, C = list(map(int, input().split()))

for i in range(X//1000, -1, -1):
    if i*1000 + C*i > X:
        continue

    print(i*1000)
    break