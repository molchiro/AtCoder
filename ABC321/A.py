N = input()
if list(N) == sorted(list(N), reverse=True) and len(N) == len(set(list(N))):
    print('Yes')
else:
    print('No')