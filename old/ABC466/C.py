N = int(input())
ans = 0

r = 1
for i in range(1, N+1):
    r = max(r, i)
    while r+1 <= N:
        print('?', i, r+1)
        if input() == 'No':
            break
        else:
            r += 1
        # print(r)

    ans += r-i

print('!', ans)