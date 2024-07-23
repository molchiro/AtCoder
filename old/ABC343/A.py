A, B = list(map(int, input().split()))
for i in range(10):
    if i != A+B:
        print(i)
        exit()