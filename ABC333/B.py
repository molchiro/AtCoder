Edges = {'AB', 'BC', 'CD', 'DE', 'EA', 'AE', 'ED', 'DC', 'CB', 'BA'}
S = input()
T = input()
if S in Edges and T in Edges:
    print(('Yes'))
elif S not in Edges and T not in Edges:
    print(('Yes'))
else:
    print('No')