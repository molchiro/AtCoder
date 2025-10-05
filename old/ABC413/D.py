from math import gcd

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    s = set([abs(a) for a in A])

    if len(set(A)) == 1:
        # r = 1のとき
        print('Yes')
    elif len(s) == 1:
        # r = -1 として成立するか判定
        if N%2 == 0:
            print('Yes' if sum(A) == 0 else 'No')
        else:
            print('Yes' if abs(sum(A)) == s.pop() else 'No')
    else:

        A.sort(key=lambda x: abs(x))
        r = [(A[1] // gcd(A[1], A[0]), A[0] // gcd(A[1], A[0])), (-A[1] // gcd(A[1], A[0]), -A[0] // gcd(A[1], A[0]))]
        for i in range(1, N-1):
            if (A[i+1] // gcd(A[i+1], A[i]), A[i] // gcd(A[i+1], A[i])) not in r:
                print('No')
                break
        else:
            print('Yes')