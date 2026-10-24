N = int(input())
X = list(map(int, input().split()))
f = 1
for x in X:
    if x >= 0:
        f = 0

print('Yes' if f else 'No')