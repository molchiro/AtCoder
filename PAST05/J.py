S = input()
X = int(input())-1
T = 0
num = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
r = len(S)
for i in range(len(S)):
    s = S[i]
    if s in num:
        T *= int(s)+1
    else:
        T += 1
    if T > X:
        r = i
        break

for i in range(r, -1, -1):
    # print(T, X)
    s = S[i]
    if s in num:
        T //= int(s)+1
        X %= T
    else:
        T -= 1
        if T == X:
            print(s)
            exit()