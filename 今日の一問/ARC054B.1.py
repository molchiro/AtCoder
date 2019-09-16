def f(x, P):
    return x + P/(2**(x/1.5))

P = float(input())

left = 0
right = 100

while abs(f(left, P) - f((left+right)/2, P)) > 10**(-9) and abs(f(right, P) - f((left+right)/2, P)) > 10**(-9):
    d = (right - left) / 3
    if f(right - d, P) - f(left + d, P) > 0:
        right -= d
    else:
        left += d
print(f((left+right)/2, P))