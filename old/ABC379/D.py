Q = int(input())

day = 0
picked = -1
setted = -1
plants = [None]*(10**6)

for _ in range(Q):
    query = input()

    if query == '1':
        setted += 1
        plants[setted] = day
    else:
        x, y = query.split()
        if x == '2':
            T = int(y)
            day += int(T)
        else:
            H = int(y)

            ok = picked
            ng = setted + 1
            while ng - ok > 1:
                test = (ng+ok)//2
                if day-plants[test] >= H:
                    ok = test
                else:
                    ng = test
            
            print(ok - picked)
            picked = ok