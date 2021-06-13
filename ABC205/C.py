A, B, C = list(map(int, input().split()))
if A == B:
    # 3 3 3
    print('=')
elif A == 0:
    if B < 0:
        if C%2:
            # 0 -2 3
            print('>')
        else:
            # 0 -2 4
            print('<')
    else:
        # 0 2 3
        print('<')
elif B == 0:
    if A < 0:
        if C%2:
            # -2 0 3
            print('<')
        else:
            # -2 0 4
            print('>')
    else:
        # 2 0 4
        print('>')
elif A*B < 0:
    if C%2 == 0:
        if abs(A) == abs (B):
            # -2 2 4
            print('=')
        elif abs(A) < abs (B):
            # -2 3 4
            print('<')
        else:
            # -3 2 4
            print('>')
    else:
        if A < B:
            # -3 2 3
            print('<')
        else:
            # 3 -4 3
            print('>')
else:
    if abs(A) < abs (B):
        # 5 6 3
        print('<')
    else:
        # 7 6 3
        print('>')