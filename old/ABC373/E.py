from bisect import bisect_left, bisect_right

N, M, K = list(map(int, input().split()))
A = list(map(int, input().split()))

if N == M:
    print(*[0]*N)
    exit()

K -= sum(A)

A_sorted = sorted(A)
cumsum = [0]
for a in A_sorted:
    cumsum.append(a+cumsum[-1])
A_left_dic = {}
prev = -1
for i, a in enumerate(A_sorted):
    if a == prev:
        continue
    A_left_dic[a] = i
    prev = a

# print(cumsum)

# print(A_left_dic)

# 現在a票の人がプラスx票取った時、aが負ける条件が成立しないなら成功
def judge(a, x):
    # print(a, x)
    global A_sorted, A_left_dic, cumsum, N, M, K 

    y = a+x+1
    
    idx = A_left_dic[a]
    l = N - M
    r = max(l, bisect_right(A_sorted, y))
    needed = x + y*(r-l)
    # print(needed)

    if l <= idx:
        # print('if',l, r)
        needed -= cumsum[r]-cumsum[l-1]-a
    else:
        # print('else', l, r)
        needed -= cumsum[r]-cumsum[l]

    return needed > K

ans = []
for a in A:
    l = -1
    r = 10**13
    while r - l > 1:
        test = (l+r)//2
        if judge(a, test):
            r = test
        else:
            l = test

    # print('finish',a, l, r, K)

    if r <= K and judge(a, r):
        ans.append(r)
    else:
        ans.append(-1)

print(*ans)