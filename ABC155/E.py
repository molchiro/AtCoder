N = input()
res = 0
for s in N:
    s = int(s)
    if s < 6:
        res += s
    else:
        res += 1 + (10-s)
print(res)
