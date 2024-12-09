S = input().split()
if S == ['>', '>', '>']:
    print('B')
if S == ['>', '>', '<']:
    print('C')
if S == ['<', '>', '>']:
    print('A')
if S == ['<', '<', '>']:
    print('C')
if S == ['>', '<', '<']:
    print('A')
if S == ['<', '<', '<']:
    print('B')