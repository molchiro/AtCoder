import math

A, B, H ,M = list(map(int, input().split()))

Atheta = (H+M/60)/12*360
Btheta = M/60*360
Ax = A*math.sin(math.radians(Atheta))
Ay = A*math.cos(math.radians(Atheta))
Bx = B*math.sin(math.radians(Btheta))
By = B*math.cos(math.radians(Btheta))

print(math.sqrt(pow(Ax-Bx, 2) + pow(Ay-By, 2)))