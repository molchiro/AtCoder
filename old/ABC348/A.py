N = int(input())
for i in range(N):
    print('o' if (i+1)%3 else 'x', end='')
print()