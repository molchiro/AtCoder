N = int(input())
for i in range(1000000):
    if N >> i & 1:
        print(i)
        break