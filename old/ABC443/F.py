
N = int(input())

if N%10 == 0:
    print(-1)
    exit()

def judge(x):
    if x == 0:
        return 0
    
    global N
    y = x*N
    S = str(y)
    prev = S[0]
    f = 1
    for s in S:
        if int(prev) > int(s):
            f = 0
        prev = s
    return f

def judge_partial(x, d):
    if x == 0:
        return 0
    
    global N
    y = x*N
    S = str(y)[-d::]
    if S[0] == '0':
        return 0
    
    prev = S[0]
    f = 1
    for s in S:
        if int(prev) > int(s):
            f = 0
        prev = s
    return f

# 1の位から順に採用しても良い組み合わせを確定していく
d = 1
dp = ['']
while True:
    ndp = []
    for p in dp:
        for i in range(10):
            x = int(str(i)+p)
            # 条件を満たすか
            if judge(x):
                print(x*N)
                exit()
            # 部分的に条件を満たすか
            if judge_partial(x, d):
                ndp.append(str(i)+p)
    dp = ndp
    d += 1

    print(dp)
    print([str(int(x)*N) for x in dp])
    print([str(int(x)*N)[-d+1::] for x in dp])
    print(len(dp))
    input()
