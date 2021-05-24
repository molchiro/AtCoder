ans = []
for s in input():
    if s == '6':
        s = '9'
    elif s == '9':
        s = '6'
    ans.append(s)
print(''.join(ans[::-1]))