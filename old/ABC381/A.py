N = int(input())
S = input()
if S == '/':
    print('Yes')
    exit()
if S.count('/') != 1:
    print('No')
    exit()

S_ = S.split('/')
if len(S_) != 2:
    print('No')
    exit()
if len(S_[0]) != len(S_[1]):
    print('No')
    exit()


if set(list(S_[0])) == {'1'} and set(list(S_[1])) == {'2'}:
    print('Yes')
else:
    print('No')
