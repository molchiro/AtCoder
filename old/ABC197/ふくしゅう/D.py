from math import cos, sin, pi

N = int(input())
x0, y0 = list(map(int, input().split()))
x1, y1 = list(map(int, input().split()))
z = x0 + y0*1j
O = (x0+x1)/2 + (y0+y1)/2*1j
th = 2*pi/N
ans = (z-O)*(cos(th)+sin(th)*1j)+O
print(ans.real, ans.imag)
