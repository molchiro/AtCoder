x, y = list(map(int, input().split()))
if x == y:
    print(x)
else:
    print(list({0, 1, 2} - {x} - {y})[0])