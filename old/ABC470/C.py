N, Q = list(map(int, input().split()))

d = dict()
d[0] = N
A = [0] * N
offset = 0

ans = 0

for _ in range(Q):
    ipt = input()
    if ipt == '2':
        ans = 0
        if offset in d:
            if offset + 1 in d:
                d[offset+1] += d[offset]
            else:
                d[offset+1] = d[offset]
            d.pop(offset)
        offset += 1
        for k, v in d.items():
            if v%2:
                ans ^= k-offset

    else:
        _, x = list(map(lambda x: int(x) - 1, ipt.split()))
        if A[x] < offset:
            A[x] = offset
        ans ^= A[x] - offset
        d[A[x]] -= 1
        if d[A[x]] == 0:
            d.pop(A[x])
        A[x] += 1
        if not A[x] in d:
            d[A[x]] = 1
        else:
            d[A[x]] += 1
        ans ^= A[x] - offset


    # print(offset, A, d)
    print(ans)