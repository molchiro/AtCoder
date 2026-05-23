X = list(input())

Y = [x for x in X if x != '0']
Z = [x for x in X if x == '0']
Y.sort()

ans = Y[0]
Y = Y[1:]
print(ans + ''.join(Z) + ''.join(Y))