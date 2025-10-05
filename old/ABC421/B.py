def f(x):
    s = str(x)
    return int(s[::-1])

l = list(map(int, input().split()))

for _ in range(8):
    l.append(f(l[-1]+l[-2]))

print(l[-1])