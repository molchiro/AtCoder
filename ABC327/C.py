A = [list(map(int, input().split())) for _ in range(9)]

def _check(l):
    return len(set(l)) == len(l)

def check_row(i):
    global A
    return _check(A[i])

def check_col(i):
    global A
    # print('col', [A[j][i] for j in range(9)])
    return _check([A[j][i] for j in range(9)])

def check_box(i, j):
    global A
    box = A[i][j:j+3] + A[i+1][j:j+3] + A[i+2][j:j+3]
    return _check(box)

def check():
    global A
    for i in range(9):
        if not check_row(i):
            return False
    for i in range(9):
        if not check_col(i):
            return False
    for i in range(3):
        for j in range(3):
            if not check_box(i*3, j*3):
                return False

    return True

print('Yes' if check() else 'No')