coockies = list(map(int, input().split()))
ans = 'No'
half = sum(coockies)/2
patterns = ['1000', '0100', '0010', '0001', '1100', '1010', '1001']
for p in patterns:
    tmp = 0
    for i in range(4):
        if p[i] == '1':
            tmp += coockies[i]
    if tmp == half:
        ans = 'Yes'
print(ans)
        