N, Q = list(map(int, input().split()))
S = input()

cumsum_1 = [0]
cumsum_2 = [0]
where_slash = []
ct_1 = 0
ct_2 = 0
for i, s in enumerate(list(S)):
    if s == '1':
        ct_1 += 1
    elif s == '2':
        ct_2 += 1
    else:
        where_slash.append(i)
    cumsum_1.append(ct_1)
    cumsum_2.append(ct_2)

# print(cumsum_1)
# print(cumsum_2)
# print(where_slash)

from bisect import bisect_left, bisect_right

for _ in range(Q):
    L, R = list(map(lambda x: int(x) - 1, input().split()))

    l = bisect_left(where_slash, L)
    r = bisect_right(where_slash, R)-1

    if l > r:
        print(0)
        continue
    
    while r - l > 1:
        m = (r+l)//2
        M = where_slash[m]
        ones = cumsum_1[M]-cumsum_1[L]
        twos = cumsum_2[R+1]-cumsum_2[M]
        if ones < twos:
            l = m
        else:
            r = m

    # print(L, R, l, r)
    ans1 = min(cumsum_1[where_slash[l]]-cumsum_1[L], cumsum_2[R+1]-cumsum_2[where_slash[l]+1])
    ans2 = min(cumsum_1[where_slash[r]]-cumsum_1[L], cumsum_2[R+1]-cumsum_2[where_slash[r]+1])

    print(max(ans1, ans2)*2+1)




