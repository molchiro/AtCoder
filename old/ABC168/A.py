N = input()
N_ = int(N[-1])
if N_ == 3:
    print('bon')
elif N_ in [0, 1, 6, 8]:
    print('pon')
else:
    print('hon')