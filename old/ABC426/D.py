T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input())
    prev = ''
    ct = 0
    rl = []
    for s in S:
        if s == prev:
            ct += 1
        else:
            rl.append((prev, ct))
            ct = 1
        prev = s
    rl.append((prev, ct))
    zeros = []
    ones = []
    for k, v in rl:
        if k == '0':
            zeros.append(v)
        else:
            ones.append(v)
    zeros.sort()
    ones.sort()
    # print(zeros, ones)
    print(min( sum(zeros[:-1])*2 + sum(ones) , sum(zeros) + sum(ones[:-1])*2))