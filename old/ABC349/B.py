C = input()
temp = [0]*26
for c in C:
    o = ord(c) - ord('a')
    temp[o] += 1
# print(temp)
for x in temp:
    if x == 0:
        continue
    cnt = 0
    for y in temp:
        if x == y:
            cnt += 1
    # print(x, cnt)
    if cnt == 0 or cnt == 2:
        continue

    print('No')
    break
else:
    print('Yes')
