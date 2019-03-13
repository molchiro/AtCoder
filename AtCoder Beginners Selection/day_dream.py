S = input()
S = "".join([x for x in S.split('eraser') if x])
S = "".join([x for x in S.split('erase') if x])
S = "".join([x for x in S.split('dreamer') if x])
S = "".join([x for x in S.split('dream') if x])
if len(S) == 0:
  print('YES')
else:
  print('NO')
