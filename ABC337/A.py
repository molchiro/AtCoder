N = int(input())
t = 0
a = 0
for _ in range(N):
    x, y = list(map(int, input().split()))
    t += x
    a += y

if t == a:
    print('Draw')
elif t > a:
    print('Takahashi')
else:
    print('Aoki')