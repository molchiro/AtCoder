A, B, C = list(map(int, input().split()))

awake = [0]*24

x = C
while x != B:
    awake[x] = 1
    x += 1
    x %= 24

print('Yes' if awake[A] else 'No')