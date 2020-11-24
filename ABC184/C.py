def f(s, t):
    if s[0] + s[1] == t[0] + t[1]:
        return True
    elif s[0] - s[1] == t[0] - t[1]:
        return True
    elif abs(s[0]-t[0]) + abs(s[1]-t[1]) <= 3:
        return True
    else:
        return False


s = list(map(int, input().split()))
t = list(map(int, input().split()))

if s == t:
    print(0)
elif f(s, t):
    print(1)
else:
    U = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            U.append([t[0]+i, t[1]+j])
    U.append([t[0], t[1]-3])
    U.append([t[0], t[1]+3])
    U.append([t[0]-3, t[1]])
    U.append([t[0]+3, t[1]])
    for u in U:
        if f(s, u):
            print(2)
            exit()
    
    if s[0] > t[0]:
        s, t = t, s
    tmp = t[0] - s[0]
    if min(abs(t[1]-s[1]+tmp), abs(t[1]-s[1]-tmp))%2 == 0:
        print(2)
        exit()        
    print(3)