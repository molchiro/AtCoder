T = int(input())
for _ in range(T):
    N, A, B = list(map(int, input().split()))

    if N%2:
        print('No')
        continue
    if (A+B)%2==0:
        print('No')
        continue

    print('Yes')

    pre = ''
    post = ''
    H = N
    W = N
    now = [1, 1]

    # 上
    for _ in range((A-1)//2):
        pre += 'R'*(W-1) + 'D'
        pre += 'L'*(W-1) + 'D'
        H -= 2
        now[0] += 2

    # 左
    for _ in range((B-1)//2):
        pre += 'D'*(H-1) + 'R'
        pre += 'U'*(H-1) + 'R'
        W -= 2
        now[1] += 2

    mid = 'DR' if now[0] == A else 'RD'


    # 下
    for _ in range((N-A)//2):
        post += 'R'*(W-1) + 'D'
        post += 'L'*(W-1) + 'D'
        H -= 2

    # 右
    for _ in range((N-B)//2):
        post += 'D'*(H-1) + 'R'
        post += 'U'*(H-1) + 'R'
        W -= 2


    # print(pre+'-'+mid+'-'+post[::-1])
    print(pre+mid+post[::-1])

# ....
# ....
# .#..
# ....