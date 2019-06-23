S = input()
tmp = ''
f = 0
for s in S:
    if s == tmp:
        f = 1
    tmp = s
if f == 1:
    print('Bad')
else:
    print('Good')