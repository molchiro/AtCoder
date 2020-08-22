N = input()
print('Yes' if sum([int(x) for x in N])%9 == 0 else 'No')