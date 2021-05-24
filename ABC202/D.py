factorial = [None]*61
factorial[0] = 1
def calc_factorial(n):
    if factorial[n] == None:
        factorial[n] = n*calc_factorial(n-1)
    return factorial[n]
def f(i, j):
    return calc_factorial(i+j)//calc_factorial(i)//calc_factorial(j)

A, B, K = list(map(int, input().split()))
ans = ''
A_rem = A
B_rem = B
for i in range(A+B):
    n = f(A_rem-1, B_rem)
    if n >= K:
        ans = ans + 'a'
        A_rem -= 1
    else:
        ans = ans + 'b'
        B_rem -= 1
        K -= n
    if A_rem*B_rem == 0:
        break
    # print(ans, n)
print(ans+'a'*A_rem+'b'*B_rem)