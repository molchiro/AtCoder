ans = []
while True:
    s = input()
    ans.append(s)
    if s == '0':
        break

for i in range(len(ans)):
    print(ans[-1-i])