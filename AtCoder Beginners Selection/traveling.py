def can_move(current, target):
  dist = abs(target[1] - current[1]) + abs(target[2] - current[2])
  dt = target[0] - current[0]
  if dist > dt:
    return False
  elif (dist + dt)%2 != 0:
    return False
  else:
    return True
  
N = int(input())
current = [0, 0, 0]
status = 'Yes'
for i in range(N):
  target = list(map(int, input().split()))
  if can_move(current, target):
    current = target[:]
  else:
    status = 'No'
    break
print(status)
