def check_alive(n):
    p = n
    for spell in spells:
        if spell[0] == s[p]:
            p += 1 if spell[1] == 'R' else -1
        if p == -1:
            return 'L'
        elif p == N:
            return 'R'
    return 'OK'

N, Q = list(map(int, input().split()))
s = [x for x in input()]
spells = [input().split() for i in range(Q)]

def __main__():
    if check_alive(0) == 'R':
        print(0)
        return
    elif check_alive(0) == 'OK':
        left_alive = 0
    else:
        a, b = 0, N-1
        while b - a > 1:
            m = round((b+a)/2)
            if check_alive(m) == 'L':
                a = m
            else:
                b = m
        left_alive = b
    if check_alive(N-1) == 'L':
        print(0)
        return
    elif check_alive(N-1) == 'OK':
        right_alive = N-1
    else:
        a, b = 0, N-1
        while b - a > 1:
            m = round((b+a)/2)
            if check_alive(m) == 'R':
                b = m
            else:
                a = m
        right_alive = a
    
    print(right_alive - left_alive + 1)

if __name__ == "__main__":
    __main__()
