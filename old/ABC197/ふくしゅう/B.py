H, W, X, Y = list(map(int, input().split()))
field = []
field.append('#'*(W+2))
for _ in range(H):
    S = input()
    field.append('#'+S+'#')
field.append('#'*(W+2))

ans = 0

x, y = X, Y
while field[x][y] == '.':
    ans += 1
    x += 1

x, y = X, Y
while field[x][y] == '.':
    ans += 1
    x -= 1

x, y = X, Y
while field[x][y] == '.':
    ans += 1
    y += 1
    
x, y = X, Y
while field[x][y] == '.':
    ans += 1
    y -= 1

ans -= 3

print(ans)