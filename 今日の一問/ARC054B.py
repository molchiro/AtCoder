def slope(x, P):
    def finish_time(x, P):
        return x + P/(2**(x/1.5))
    return (finish_time(x+10**(-8), P) - finish_time(x, P))*10**8

P = float(input())
left = 0
right = 100
if slope(left, P) > 0:
    pass
elif slope(right, P) < 0:
    print('error')
else:
    while right - left > 10**(-12):
        half = (right + left) / 2
        if slope(half, P) > 0:
            right = half
        else:
            left = half
print(left + P/(2**(left/1.5)))