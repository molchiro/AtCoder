H, A = list(map(int, input().split()))
i = 0
while H > 0:
    i += 1
    H -= A
print(i)