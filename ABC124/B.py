N = int(input())
H = list(map(int, input().split()))

temp = 0
ct = 0
for h in H:
    if h >= temp:
        ct += 1
        temp = h

print(ct)