A, B = list(map(int, input().split()))
res = abs((A+B)/2)
if res == int(res):
    print(int(res))
else:
    print('IMPOSSIBLE')