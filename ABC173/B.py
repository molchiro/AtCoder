from collections import Counter

N = int(input())
c = Counter([input() for _ in range(N)])

print('AC x ' + str(c['AC']))
print('WA x ' + str(c['WA']))
print('TLE x ' + str(c['TLE']))
print('RE x ' + str(c['RE']))